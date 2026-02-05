from rest_framework import serializers 
from .models import Restaurant

class restaurant_serializer(serializers.ModelSerializer) :
    class Meta :
        model = Restaurant
        fields = [ "name", "logo", "adresse" ]