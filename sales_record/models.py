from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from customer.models import customer


class sales_record(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    name = models.CharField(max_length=50, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)
    brand = models.CharField(max_length=150, null=True, blank=True)
    total_price = models.IntegerField(blank=True, null=True)
    Payment_mode = models.CharField(max_length=150, blank=True, null=True)
    bought_by = models.ForeignKey(customer, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.name} {self.brand}"
