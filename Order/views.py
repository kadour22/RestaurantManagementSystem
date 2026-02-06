from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.db import transaction

from .serializers import *
from .models import *

class order_service(APIView) :

    def get(self, request) :
        orders = Order.objects.select_related("table").all()
        serializer = OrderItemListSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request) :
        serializer = order_service(data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



        

