from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View

from store.models.product import Product
from store.models.orders import Order


class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        print(address, phone, customer, cart, products)
        orders = Order.get_all_orders()
        for product in products:
            print(cart.get(str(product.id)))
            quantity_temp = 0
            for order in orders:
                if product.id == order.product.id and order.status == False and order.address == address:
                    Order.objects.filter(id=order.id).delete()
                    quantity_temp += order.quantity
            order = Order(customer=Customer(id=customer),
                          product=product,
                          price=product.price,
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(product.id)) + quantity_temp
                          )
            order.save()
        request.session['cart'] = {}

        return redirect('cart')
