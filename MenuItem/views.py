from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .serializers import MenuItemSerializer
from .models import MenuItem

class MenuItemViewSet(ModelViewSet) :
    permission_classes = [IsAdminUser]
    queryset = MenuItem.objects.select_related('category').all()
    serializer_class = MenuItemSerializer
