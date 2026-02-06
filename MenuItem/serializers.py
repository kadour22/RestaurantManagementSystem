from rest_framework import serializers
from .models import MenuItem
from Category.serializers import category_serializer

class MenuItemSerializer(serializers.ModelSerializer) :
    
    class Meta :
        model = MenuItem
        fields = ["name","price","description","image","category"]