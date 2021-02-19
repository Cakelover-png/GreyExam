from django.shortcuts import render, redirect
from django.http import HttpResponse
from user.forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout


def user_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('ecommerce:home')
    return HttpResponse(status=405)


def user_login(request):
    if request.user.is_authenticated:
        return redirect('ecommerce:home')
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('ecommerce:home')

    return render(
        request,
        'user/login.html',
        context={
            'form': form
        }
    )


def register(request):
    if request.user.is_authenticated:
        return redirect('ecommerce:home')
    user_create_form = CustomUserCreationForm()
    if request.method == 'POST':
        user_create_form = CustomUserCreationForm(
            request.POST)
        if user_create_form.is_valid():
            user_create_form.save()
            return redirect('ecommerce:home')

    return render(
        request,
        template_name='user/register.html',
        context={
            'form': user_create_form
        }
    )
