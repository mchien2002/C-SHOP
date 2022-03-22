from django.contrib import admin
from .models.product import Product
# Register your models here.
# tạo site Product cho admin
admin.site.register(Product)
