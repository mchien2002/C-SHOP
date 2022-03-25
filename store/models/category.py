# DANH MỤC CỦA MODEL
from pyexpat import model
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=30)

    # Hiện danh mục sản phẩm ở mục Product/Category
    def __str__(self):
        return self.name