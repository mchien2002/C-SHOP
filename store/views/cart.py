from django.views import View 
from django.shortcuts import render, redirect
from store.models.category import Category
from store.models.customer import Customer
from django.contrib.auth.hashers import check_password, make_password
from store.models.product import Product
from store.models.product_detail import ProductDetail

# CHIEN: Class base View
class Cart(View):
    def get(self, request):
        ids=list(request.session.get('cart').keys())

        product_details=ProductDetail.get_productDetails_by_id((ids))
        categories = Category.get_all_categories()
        return render(request, 'cart.html', {'productDetails':product_details, 'categories': categories})
