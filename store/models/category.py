# CHIEN: DANH MỤC CỦA MODEL
from pyexpat import model
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=30)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    # CHIEN: Hiện danh mục sản phẩm ở mục Product/Category
    def __str__(self):
        return self.name