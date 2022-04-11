from operator import ge
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import register_converter
from sympy import product
from store.models.product import Product
from store.models.category import Category
from django.views import View
# Create your views here.

class Index(View):
    def post(self, request):
        product = request.POST.get('product')
        # CHIEN: Thêm sản phẩm vào dỏ hàng
        cart = request.session.get('cart')
        if cart:
            quanlity = cart.get(product)
            if quanlity:
                cart[product] = quanlity + 1
            else:   
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        print(request.session.get('cart'))
        return redirect('homepage')

    def get(self, request):
        cart=request.session.get('cart')
        if not cart:
            request.session.cart={}
        products = None
        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')
        if categoryID:
            products = Product.get_all_products_by_categoryid(categoryID)
        else:
            products = Product.get_all_products()
        # Chien: TẠO THƯ VIỆN DATA RỒI TRUYỀN DỮ LIỆU CỦA PRODUCT VS CATEGORY CHO INDEX.HTML XỬ LÝ
        data = {}
        data['products'] = products
        data['categories'] = categories
        print('customer: ' + str(request.session.get('email')))
        return render(request, 'index.html', data)

    


   
