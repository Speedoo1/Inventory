from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from sales_record.models import sales_record


def index(request):
    sale = sales_record.objects.all()
    sums = 0
    for i in sale:
        sums = sums + int(i.total_price)
    context = {'data': sale, 'sum': sums}
    return render(request, 'sales_record/home.html', context)


@login_required(login_url='base:login')
def add_record(request):
    if request.method == 'POST':
        stock_name = request.POST.get('stock')
        Qty = request.POST.get('Qty')
        price = request.POST.get('price')
        brand = request.POST.get('brand')
        available = request.POST.get('available')
        payment = request.POST.get('payment')
        total = int(Qty) * int(price)
        store = sales_record(username=request.user, name=stock_name, quantity=Qty, price=price,
                             brand=brand, Payment_mode=payment, total_price=total)
        if store:
            store.save()
            messages.success(request, 'Item Added successfully')
            return redirect('sales:index')

    return render(request, 'sales_record/add_record.html')


def single_sales(request, pk):
    sales = sales_record.objects.get(id=pk)
    context = {'data': sales}
    return render(request, 'sales_record/record.html', context)


@login_required(login_url='base:login')
def update_record(request, pk):
    sale = sales_record.objects.get(id=pk)
    if request.method == 'POST':
        stock_name = request.POST.get('stock')
        Qty = request.POST.get('Qty')
        price = request.POST.get('price')
        brand = request.POST.get('brand')

        payment = request.POST.get('payment')
        total = int(Qty) * int(price)

        sale.price = price
        sale.brand = brand
        sale.Payment_mode = payment
        sale.total_price = total
        sale.name = stock_name
        sale.quantity = Qty
        if sale:
            sale.save()
            messages.success(request, 'Item updated Successfully')
            return redirect('sales:index')

    context = {'data': sale}
    return render(request, 'sales_record/update_record.html', context)


@login_required(login_url='base:login')
def delete_record(request, pk):
    sale = sales_record.objects.get(id=pk)
    sale.delete()
    messages.error(request, 'Sales Deleted Successfully')
    return redirect('sales:index')
