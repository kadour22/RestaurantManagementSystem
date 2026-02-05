from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from .models import Table
from .serializers import table_serializer

class table_services(APIView) :

    def get(self, request) :

        tables = Table.objects.select_related('restaurant').all()
        serializer = table_serializer(tables, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request) :
        serializer = table_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        with transaction.atomic() :
            instance = serializer.save()
        
        return Response(
            table_serializer(instance).data,
            status=status.HTTP_201_CREATED            
            )

