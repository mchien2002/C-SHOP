from django.views import View 
from django.shortcuts import render, redirect
from store.models.customer import Customer
from django.contrib.auth.hashers import check_password, make_password
from store.models.product import Product

# CHIEN: Class base View
class Cart(View):
    def get(self, request):
        ids=list(request.session.get('cart').keys())
        products=Product.get_products_by_id((ids))
        print(products)
        return render(request, 'cart.html', {'products':products})
