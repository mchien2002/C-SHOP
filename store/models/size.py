from pyexpat import model
from django.db import models
from matplotlib import style

class Size(models.Model):
    name = models.CharField(max_length=20)
    style_product = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    @staticmethod
    def get_all_size():
        return Size.objects.all()
    @staticmethod
    def get_size_by_styleProduct(styleProduct):
        return Size.objects.filter(style_product = styleProduct)