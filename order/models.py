from django.db import models

from account.models import Customer
from base.models import TimeStampedModel
from product.models import Product


class Order(TimeStampedModel):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='order')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order')
    quantity = models.IntegerField(default=1)
    total_prise = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.quantity} * {self.product.prise} = {self.total_prise}'


class OrderItem(TimeStampedModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orderitem')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orderitem')
    total_prise = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.total_prise}'
