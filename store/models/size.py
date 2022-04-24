from pyexpat import model
from django.db import models

class Size(models.Model):
    name = models.CharField(max_length=20)
    style_product = models.CharField(max_length=20)

    def __str__(self):
        return self.name