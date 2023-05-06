from django.urls import path

from sales_record import views

app_name = 'sales'
urlpatterns = [

    path('', views.index, name='index'),
    path('add-record', views.add_record, name='add-record'),
    path('sales-info/<str:pk>', views.single_sales, name='info'),
    path('update/<str:pk>', views.update_record, name='update-info'),
    path('delete/<str:pk>', views.delete_record, name='delete')

]
