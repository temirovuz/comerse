from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect

from account.forms import RegisterForm, LoginForm
from account.models import User


# def sign_up(request):
#     if request.method == 'POST':
#         form = RegisterForm()
#         return render(request, 'account/registration.html', {'form': form})
#
#
# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
#             if user:
#                 login(request, user)
#                 return redirect('home')
#     else:
#         form = LoginForm()
#     return render(request, 'account/login.html', {'form': form})

def Register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        password2 = request.POST['password2']
        if password != password2:
            return HttpResponse('Password does not')
        else:
            phone = request.POST.get('phone')
            print(username, email, password, password2, phone)
            my_user = User.objects.create_user(username=username, email=email, password=password, phone_numer=phone)
            my_user.save()
            return redirect('account:login')
    return render(request, 'account/registration.html')


def Login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('base:home')
        else:
            return HttpResponse("Invalid username or password")
    return render(request, 'account/login.html')


def Logout_user(request):
    return render(request, 'account/home.html')
