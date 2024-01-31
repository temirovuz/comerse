from django.contrib import admin

from product.models import Product, Images

# Register your models here.
admin.site.register([Product, Images])