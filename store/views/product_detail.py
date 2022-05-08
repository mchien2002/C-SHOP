from math import prod
from django.shortcuts import redirect, render
from django.views import View
from store.models.cart import Cart
from store.models.customer import Customer

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
        customer = request.session.get('customer')
        cart_quantity = request.POST.get('quantity')
        if cart_quantity == '':
            cart_quantity = 1
        

        carts = Cart.get_carts_by_customer(customer)
        quantity_temp = 0
        for cart in carts:
            if cart.size == size and cart.product == product:
                quantity_temp = cart.quantity
                Cart.objects.filter(id = cart.id).delete()
                
        cart = Cart(
            customer = Customer(id = customer),
            product=product,
            size=size,
            quantity = int(cart_quantity) + quantity_temp,
            price = product.price *  int(cart_quantity) + quantity_temp,
        )
        cart.save()
        return redirect('cart')