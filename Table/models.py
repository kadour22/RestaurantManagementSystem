from django.db import models
from Restaurant.models import Restaurant
from uuid import uuid4

class Table(models.Model) :
    table_number = models.CharField(max_length=2)
    table_uuid = models.CharField(max_length=200, default=uuid4)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='table')

    def __str__(self):
        return f"{self.restaurant.name} {self.table_number}"