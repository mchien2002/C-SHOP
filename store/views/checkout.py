from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View

from store.models.product import Product
from store.models.orders import Order
from store.models.product_detail import ProductDetail


class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        productDetails = ProductDetail.get_productDetails_by_id(list(cart.keys()))

        orders = Order.get_all_orders()
        for productDetail in productDetails:
            quantity_temp = 0
            for order in orders:
                if productDetail.id == order.product_detail.id and order.status == False and order.address == address and productDetail.size == order.product_detail.size:
                    Order.objects.filter(id=order.id).delete()
                    quantity_temp += order.quantity
            order = Order(customer=Customer(id=customer),
                          product_detail=productDetail,
                          price=productDetail.product.price,
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(productDetail.id)) + quantity_temp
                          )
            order.save()
        request.session['cart'] = {}

        return redirect('cart')
