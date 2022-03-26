from distutils.command.upload import upload
from pyexpat import model
from statistics import mode
from django.db import models
from .category import Category
from store.models import category
# Create your models here.
class Product(models.Model):
    # CHIEN: tên sp
    name = models.CharField(max_length=50)
    # CHIEN: giá sp
    price = models.IntegerField(default=0)
    # CHIEN: mô tả sp
    description = models.CharField(max_length=200, default=0)
    # CHIEN: thương hiệu của sản phẩm
    thuonghieu = models.CharField(max_length=50, default='Unknown')
    # CHIEN: ảnh minh họa sp
    image = models.ImageField(upload_to='uploads/products/')
    # CHIEN: Tạo khóa ngoại category để xác định product này thuộc loại quần áo nào
    # CHIEN: on_delete = models.cascade: dữ liệu con sẽ bị xóa nếu dữ liệu trong bảng mẹ bị xáo
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default='Unknown')

    # CHIEN: staticmethod không chịu ảnh hưởng bởi class, nó chỉ việc xử lý các tham số
    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return  Product.get_all_products();