from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Stock(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    name = models.CharField(max_length=50, blank=True, null=True, )
    quantity = models.IntegerField(blank=True, null=True)
    price = models.CharField(max_length=100, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)
    brand = models.CharField(max_length=150, null=True, blank=True, )
    available = models.BooleanField(default=True, blank=True, null=True)

    def __str__(self):
        return (f"{self.name} {self.brand}")
