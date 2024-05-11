#library django
from django.db import models

#Create Models Footer
class FooterInfo(models.Model):
    creation_date = models.DateField('Ngày tạo')
    company_name = models.CharField('Tên công ty', max_length=100)
    address = models.CharField('Địa chỉ', max_length=200)
    contact_name = models.CharField('Họ tên', max_length=100)
    phone_number = models.CharField('Số điện thoại', max_length=20)
    email = models.EmailField('Email')
    facebook_url = models.URLField('Facebook', blank=True)
    zalo_number = models.CharField('Zalo', max_length=20, blank=True)
    instagram_url = models.URLField('Instagram', blank=True)
    def __str__(self):
        return self.company_name
    
#Create Models Footer
class Product_women(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='products/')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField()
    def __str__(self):
        return self.name
    