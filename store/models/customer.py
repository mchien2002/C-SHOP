from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=500)
    mess_code = models.CharField(max_length=100)
    # CHIEN: Lưu lên database
    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email = email)
        except:
            return False
    # Kiểm tra email có tồn tại không
    def isExists(self):
        if Customer.objects.filter(email = self.email):
            return True
        return False
    def get_all_customer(self):
        return Customer.objects.all();
    
        