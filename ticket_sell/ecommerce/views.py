from django.shortcuts import render, redirect
from ecommerce.forms import OrderForm
from ecommerce.models import Order
from django.db.models import Q


def home(request):
    form = OrderForm(data=request.POST)
    if form.is_valid():
        order = form.save(commit=False)
        order.user_id = request.user.id
        order.save()
        return redirect('ecommerce:home')
    return render(request, 'ecommerce/home.html', context={"form": form})


def details(request):
    page = request.GET.get('page', 1)
    q = request.GET.get('q', None)
    if q:
        Order = Car.objects.filter(Q(user_id=request.user.id) | Q(ticket_name__icontains=q))
    else:
        Order = Car.objects.filter(user_id=request.user.id)

    return render(request, 'ecommerce/details.html')
