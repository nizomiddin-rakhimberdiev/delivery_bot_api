from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Client, UserLocation, Category, Product,Cart, Order, OrderItem


admin.site.register(Client)
admin.site.register(UserLocation)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderItem)