from django.shortcuts import render
from django.db import models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.handlers.modwsgi import groups_for_user
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import Group, User
from authen.models import Customer, Packet, Promotion, Order, Position, Service_list, Employee, Service_rate

# Create your views here.

def my_login(request):
    context = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            group = request.user.groups.all()

            if user.is_superuser or group[0].name == "Admin":
                return redirect('test')

            elif group[0].name == "User":
                return redirect('test')

        else:
            context['username'] = username
            context['password'] = password
            context['error'] = 'username หรือ password ไม่ถูกต้อง'
    next_url = request.GET.get('next')
    if next_url:
        context['next_url'] = next_url

    return render(request, 'login.html', context=context)

def my_logout(request):
    logout(request)
    return redirect('login')

def register(request):
    context = {}
    if request.method == "POST":
        check_username = User.objects.filter(username=request.POST.get('username'))
        if check_username:
            context['error'] = 'Phone number นี้ถูกใช้ไปแล้ว'
        elif request.POST.get('password') == request.POST.get('confirm'):
            user = User.objects.create_user(username=request.POST.get('username'), password=request.POST.get('password'),
            first_name=request.POST.get('firstname'), last_name=request.POST.get('lastname'))
            group = Group.objects.get(name='User')
            group.user_set.add(user)
            context['success'] = 'Sign in สำเร็จ'

            customer = Customer(cus_nname=request.POST.get('nickname'), 
            cus_fname=request.POST.get('firstname'), 
            cus_lname=request.POST.get('lastname'), 
            cus_type=request.POST.get('cus_type'), 
            cus_phone=request.POST.get('username'))
            customer.save()
        else:
            context['error'] = 'password ไม่ตรงกัน'

    return render(request, 'register.html', context=context)

@login_required
def add_order(request): #TEST
    context = {}
    return render(request, 'test.html', context=context)