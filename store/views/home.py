from operator import ge
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import register_converter
from store.models.product import Product
from store.models.category import Category

# Create your views here.

def index(request):
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_all_products_by_categoryid(categoryID)
    else:
        products = Product.get_all_products()
    # CHIEN: TẠO THƯ VIỆN DATA RỒI TRUYỀN DỮ LIỆU CỦA PRODUCT VS CATEGORY CHO INDEX.HTML XỬ LÝ
    data = {}
    data['products'] = products
    data['categories'] = categories
    return render(request, 'index.html', data)


   
