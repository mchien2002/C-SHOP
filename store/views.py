from django.shortcuts import render
from django.http import HttpResponse
from .models.product import Product
from store.models import product 
# Create your views here.

def index(request):
    # tạo list danh sách các product trong database
    prds = Product.get_all_products()
    return render(request, 'index.html', {'products': prds})