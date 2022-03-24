from distutils.command.upload import upload
from pyexpat import model
from statistics import mode
from django.db import models
from .category import Category
from store.models import category
# Create your models here.
class Product(models.Model):
    # tên sp
    name = models.CharField(max_length=50)
    # giá sp
    price = models.IntegerField(default=0)
    # mô tả sp
    description = models.CharField(max_length=200, default=0)
    # thương hiệu của sản phẩm
    thuonghieu = models.CharField(max_length=50, default='Unknown')
    # ảnh minh họa sp
    image = models.ImageField(upload_to='uploads/products/')
    # Tạo khóa ngoại category để xác định product này thuộc loại quần áo nào
    # on_delete = models.cascade: dữ liệu con sẽ bị xóa nếu dữ liệu trong bảng mẹ bị xáo
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default='Unknown')

    # staticmethod không chịu ảnh hưởng bởi class, nó chỉ việc xử lý các tham số
    @staticmethod
    def get_all_products():
        return Product.objects.all()