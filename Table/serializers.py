from rest_framework import serializers
from .models import Table

class table_serializer(serializers.ModelSerializer) :

    class Meta :
        model = Table
        fields = [ "table_number","table_uuid", "restaurant" ]