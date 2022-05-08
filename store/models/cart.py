import datetime
from operator import mod
from django.db import models
from store.models.customer import Customer
from store.models.product import Product

class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product , on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    size = models.CharField(max_length=200, default="Ngẫu nhiên")
    date = models.DateField(default=datetime.datetime.today)
    price = models.IntegerField(default=0)
    @staticmethod
    def get_carts_by_customer(customer_id):
        return Cart.objects.filter(customer = customer_id).order_by('-date')
    