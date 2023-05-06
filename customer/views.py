from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from customer.models import customer


def index(request):
    cutom = customer.objects.all()
    context = {'data': cutom}
    return render(request, 'customer/home.html', context)


def add_customer(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        last_name = request.POST.get('last_name')
        zipcode = request.POST.get('zipcode')
        gender = request.POST.get('gender')
        number = request.POST.get('number')
        city = request.POST.get('city')
        address = request.POST.get('address')
        email = request.POST.get('email')
        state = request.POST.get('state')
        custom = customer(user=request.user, first_name=name, phone=number,
                          city=city,
                          state=state,
                          address=address,
                          email=email,
                          last_name=last_name,
                          gender=gender,
                          zipcode=zipcode)
        if custom:
            custom.save()
            messages.success(request, "New customer as been Added successfully")
            return redirect('customer:index')

    return render(request, 'customer/add_record.html')


def customer_detail(request, pk):
    details = customer.objects.get(id=pk)
    context = {'data': details}
    return render(request, 'customer/record.html', context)
