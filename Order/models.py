from django.db import models
from Table.models import Table
from MenuItem.models import MenuItem


class Order(models.Model) :

    ORDER_CHOICES = (("pending","pending"),("cooking","cooking"),("served","served"),)

    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name="order")
    status = models.CharField(max_length=30,choices=ORDER_CHOICES)
    total_price = models.DecimalField(max_digits=10,decimal_places=2, null=True)
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.status

class OrderItem(models.Model) :
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name="order")
    quantity  = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.order.table.table_number} : {self.menu_item.name}"
    