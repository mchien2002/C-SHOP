from django.shortcuts import render
from django.http import HttpResponse
from .models.product import Product
from store.models import product
from .models.category import Category
# Create your views here.

def index(request):
    # CHIEN: tạo list danh sách các product trong database
    products = Product.get_all_products();
    categories = Category.get_all_categories()
    data = {}
    data['products'] = products
    data['categories'] = categories
    return render(request, 'index.html', data)