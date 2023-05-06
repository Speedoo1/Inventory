from django.urls import path

from base import views

app_name = 'base'
urlpatterns = [
    path('', views.base, name='index'),
    path('stock-add/', views.add_stock, name='add-stock'),
    path('record/<str:pk>', views.record, name='record'),
    path('delete/<str:pk>', views.delete_stock, name='delete'),
    path('update-record/<str:pk>', views.update_record, name='update'),
    path('login', views.logins, name='login'),
    path('logout', views.logouts, name='logout')

]
