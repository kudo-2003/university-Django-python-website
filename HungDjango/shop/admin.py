'''library django'''
from django.contrib import admin
from .models import FooterInfo, Product_women

admin.site.register(FooterInfo)
admin.site.register(Product_women)
