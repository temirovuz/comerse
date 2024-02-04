from django.contrib.auth.models import AbstractUser
from django.db import models

from base.models import TimeStampedModel


class User(AbstractUser, TimeStampedModel):
    TYPE_USERS = (
        (1, 'SuperAdmin'),
        (2, 'Admin'),
        (3, 'Customer'),
        (4, 'Salesman')
    )

    user_type = models.PositiveSmallIntegerField(choices=TYPE_USERS, default=3)
    phone_numer = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return self.username


class Company(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.name


class Address(models.Model):
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer', null=True)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username


class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='seller', null=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='seller', null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='seller', null=True)

    def __str__(self):
        return self.user.username
