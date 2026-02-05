
from rest_framework import generics
from .serializers import category_serializer
from .models import Category

class category_service(generics.ListCreateAPIView) :
    queryset = Category.objects.all()
    serializer_class = category_serializer