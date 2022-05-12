from email.utils import collapse_rfc2231_value
from operator import mod
from turtle import color
from django.db import models

from store.models.product import Product

class ProductDetail(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.CharField(max_length=20)
    color = models.CharField(max_length=20, default="#000000")
    
    @staticmethod
    def isExist(product_detail):
        product_details = ProductDetail.objects.all()
        for productDetail in product_details:
            if product_detail.product == productDetail.product and product_detail.size == productDetail.size and productDetail.color == color:
                return True
        return False
    @staticmethod
    def get_productDetails_by_id(ids):
        return ProductDetail.objects.filter(id__in = ids)
        
    @staticmethod
    def get_productDetail_by_product_and_size(product, size, color):
        productDetails = ProductDetail.objects.all()
        for productDetail in productDetails:
            if productDetail.product == product and productDetail.size == size and productDetail.color == color:
                return productDetail