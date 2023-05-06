from django.urls import path

from customer import views

app_name = 'customer'
urlpatterns = [
    path('', views.index, name='index'),
    path('add-customer', views.add_customer, name='add-customer'),
    path('customer-details/<str:pk>', views.customer_detail, name='customer-details')

]
