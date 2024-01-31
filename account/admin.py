from django.contrib import admin

from .models import User, Company, Address, Customer, Seller

admin.site.register([User, Company, Address, Customer, Seller])
