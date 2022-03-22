from distutils.command.upload import upload
from pyexpat import model
from django.db import models

# Create your models here.
class Product(models.Model):
    # tên sp
    name = models.CharField(max_length=50)
    # giá sp
    price = models.IntegerField(default=0)
    # mô tả sp
    description = models.CharField(max_length=200, default=0)
    # ảnh minh họa sp
    image = models.ImageField(upload_to='uploads/products/')