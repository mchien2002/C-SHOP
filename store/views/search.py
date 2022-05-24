from unicodedata import category, name
from django.shortcuts import render , redirect , HttpResponseRedirect
from sympy import ProductSet, product
from store.models.product import Product
from store.models.category import Category
from django.views import View


def search(request):
    products = None
    categories = Category.get_all_categories()
    search = request.GET.get('q')

    if search:
        products = Product.objects.filter(name__icontains = search)
    
    data = {}
    data['products'] = products
    data['categories'] = categories

    return render(request, 'index.html', data)