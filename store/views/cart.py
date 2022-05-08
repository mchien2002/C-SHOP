from django.views import View 
from django.shortcuts import render, redirect
from store.models import customer
from store.models.cart import Cart
from store.models.customer import Customer
from django.contrib.auth.hashers import check_password, make_password
from store.models.product import Product

# CHIEN: Class base View
class CartView(View):
    def get(self, request):
        customer = request.session.get('customer')
        carts = Cart.get_carts_by_customer(customer)
        total_price = 0
        for cart in carts:
            total_price += cart.price
        return render(request, 'cart.html', {'carts': carts, 'total_price': total_price})
