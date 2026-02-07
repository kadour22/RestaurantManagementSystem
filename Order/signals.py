from django.dispatch import receiver
from django.db.models.signals import pre_save
from .models import Order

# @receiver(pre_save, sender=Order)
# def calculate_total_items(sender, instance, **kwargs) :
#     total = 0
#     for x in instance.items:
#         total += x.menu_item.price * x.quantity
#     instance.total_price = total
#     return instance