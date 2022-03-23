# DANH MỤC CỦA MODEL
from pyexpat import model
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)