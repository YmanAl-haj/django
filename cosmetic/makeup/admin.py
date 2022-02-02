from django.contrib import admin
from .models import Customer,Brand,Products,Order
# Register your models here.
admin.site.register(Brand)
admin.site.register(Products)
admin.site.register(Order)
admin.site.register(Customer)