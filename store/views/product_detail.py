from math import prod
from django.shortcuts import redirect, render
from django.views import View

from store.models.product import Product

class ProductDetail(View):
    
    def get(self, request):
        product_id = request.GET.get('product_id')
        product = Product.objects.get(id = product_id)

        return render(request, 'product_detail.html', {'product': product})

    def post(self, request):
        product_id = request.POST.get('product_id')
        product = Product.objects.get(id = product_id)
        size = request.POST.get('product_size')

        cart = request.session.get('cart')

        if size:
            product.size = size
        quantity = request.POST.get('quantity')
        product.quantity = quantity
        product.save()

        if cart:
            quantity_in_cart = cart.get(product_id)
            if quantity_in_cart:
                cart[product_id]  = quantity_in_cart + int(quantity)
            else:
                cart[product_id] = 1
        else:
            cart = {}
            cart[product_id] = 1
        request.session['cart'] = cart
        return redirect('cart')