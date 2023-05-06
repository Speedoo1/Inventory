from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect

from base.models import Stock


def base(request):
    store = Stock.objects.all().order_by('-updated')
    if request.method == 'POST':
        search = request.POST.get('search')
        store = Stock.objects.filter(name__icontains=search)
    context = {'data': store}
    return render(request, 'base/home.html', context)


@login_required(login_url='base:login')
def add_stock(request):
    if request.method == 'POST':
        stock_name = request.POST.get('stock')
        Qty = request.POST.get('Qty')
        price = request.POST.get('price')
        brand = request.POST.get('brand')
        available = request.POST.get('available')
        store = Stock(username=request.user, name=stock_name, quantity=Qty, price=price, available=available,
                      brand=brand)
        if store:
            store.save()
            messages.success(request, 'Item Added successfully')
            return redirect('base:index')

    return render(request, 'base/add_record.html')


@login_required(login_url='base:login')
def record(request, pk):
    store = Stock.objects.get(id=pk)
    context = {'data': store}
    return render(request, 'base/record.html', context)


@login_required(login_url='base:login')
def update_record(request, pk):
    store = Stock.objects.get(id=pk)
    if request.method == 'POST':
        stock_name = request.POST.get('stock')
        Qty = request.POST.get('Qty')
        price = request.POST.get('price')
        brand = request.POST.get('brand')
        available = request.POST.get('available')
        store.name = stock_name
        store.quantity = Qty
        store.price = price
        store.available = available
        store.brand = brand
        if store:
            store.save()
            messages.success(request, 'Items Changed successfully')
            return redirect('base:index')
    context = {'data': store}

    return render(request, 'base/update_record.html', context)


@login_required(login_url='base:login')
def delete_stock(request, pk):
    store = Stock.objects.get(id=pk)
    store.delete()

    return redirect('base:index')


def logins(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        verify = authenticate(request, username=username, password=password)
        if verify:
            login(request, verify)
            messages.success(request, 'welcome back ' + str(request.user))
            return redirect('base:index')
        else:
            messages.error(request, 'Login Details are not correct')

    return render(request, 'base/login.html')


def logouts(request):
    logout(request)
    return redirect('base:login')
