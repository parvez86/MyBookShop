from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.db.models import OuterRef, Sum, Subquery
from django.db import connection


# Create your views here.
# def dol_to_tk(self):
#     with connection.cursor() as cursor:
#         row_price = self.
#         cursor.execute("UPDATE mysite_product SET price = price * 87.4 WHERE id = %s", [self.id])
#         cursor.execute("SELECT * FROM mysite_product WHERE id = %s", [self.id])
#         row = cursor.fetchone()
#     return row
# @login_required(login_url='/login')
def home(request):
    # dol_to_tk = 87.4
    # # products = Product.objects.raw("update lms2.mysite_product set price = price * 87.4;")
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = User.objects.get(email=email)
        print("Username: ", user.username)
        password = request.POST.get('password')

        user = authenticate(username=user.username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('mysite:index')

        else:
            messages.info(request, 'invalid credentials')
            return redirect('mysite:login')
    else:
        return render(request, 'login.html')


@login_required(login_url='/login')
def logout(request):
    auth.logout(request)
    return redirect('mysite:index')


def signup(request):
    if request.method == 'POST':
        print(request.POST.get('username'))
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('mysite:signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('mysite:signup')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email,
                                                first_name=first_name, last_name=last_name)
                if user is not None:
                    user.save()
                    print('User created!')
                    messages.success(request, 'Account is successfully created for ' + username + '!')
                    return render(request, 'login.html')
        else:
            messages.info(request, 'Password not matching..')
            return redirect('mysite:signup')
    else:
        return render(request, 'signup.html')


@login_required(login_url='/login')
def product_details(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})
