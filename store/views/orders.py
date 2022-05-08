from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View

from store.models.product import Product
from store.models.orders import Order
from store.middlewares.auth import auth_middleware


class OrderView(View):
    def get(self , request ):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        return render(request, 'orders.html' ,{'orders' : orders})
    def post(self, request):
        order = request.POST.get('remove')
        Order.objects.filter(id = order).delete()
        return redirect('orders')
   