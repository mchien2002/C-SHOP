from django.contrib import admin
from sympy import Order
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order
# Register your models here.


# CHIEN: hiện thị thông tin sản phẩm để admin dễ thao tác
class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'thuonghieu']
# CHIEN: hiển thị thông tin của danh mục sản phẩm
class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

# CHIEN: tạo site Product cho admin
admin.site.register(Product, AdminProduct)

# CHIEN: tạo site Category cho admin
admin.site.register(Category, AdminCategory)

#DANG: Tạo tài khoản Khách Hàng
admin.site.register(Customer)

admin.site.register(Order)