from django.contrib import admin
from .models.product import Product
from .models.category import Category

# Register your models here.

# tạo site Product cho admin
admin.site.register(Product)
# tạo site Category cho admin
admin.site.register(Category)
