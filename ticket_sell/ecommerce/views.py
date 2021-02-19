from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from ecommerce.forms import OrderForm
from ecommerce.models import Order
from django.db.models import Q, Count, Sum
from django.utils import timezone


def home(request):
    now = timezone.now()

    user_info = Order.objects.filter(user=request.user.id).aggregate(
        spend_money_year=Sum(
            'price',
            filter=Q(ticket__start_date__gte=now - timezone.timedelta(days=365))
        ),
        bought_last_year=Count(
            'id',
            filter=Q(ticket__start_date__gte=now - timezone.timedelta(days=365))
        ),
        spend_money_month=Sum(
            'price',
            filter=Q(ticket__start_date__gte=now - timezone.timedelta(weeks=4))
        ),
        bought_last_month=Count(
            'id',
            filter=Q(ticket__start_date__gte=now - timezone.timedelta(weeks=4))
        ),
        spend_money_week=Sum(
            'price',
            filter=Q(ticket__start_date__gte=now - timezone.timedelta(days=7))
        ),
        bought_last_week=Count(
            'id',
            filter=Q(ticket__start_date__gte=now - timezone.timedelta(days=7))
        )
    )
    form = OrderForm(data=request.POST)
    if form.is_valid():
        order = form.save(commit=False)
        order.user_id = request.user.id
        order.save()
        return redirect('ecommerce:home')
    return render(request, 'ecommerce/home.html', context={"form": form,
                                                           'user_info': user_info})


def details(request):
    page = request.GET.get('page', 1)
    q = request.GET.get('q', None)

    if q:
        order_list = Order.objects.filter(Q(user_id=request.user.id) & Q(ticket__code__icontains=q))
    else:
        order_list = Order.objects.filter(user_id=request.user.id)

    paginator = Paginator(order_list, 3)
    try:
        orders = paginator.page(page)
    except PageNotAnInteger:
        orders = paginator.page(1)
    except EmptyPage:
        orders = paginator.page(paginator.num_pages)

    return render(request, 'ecommerce/details.html', context={'orders': orders})
