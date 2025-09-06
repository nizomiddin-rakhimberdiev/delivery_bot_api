from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Client, UserLocation, Category, Product


admin.site.register(Client)
admin.site.register(UserLocation)
admin.site.register(Product)
admin.site.register(Category)