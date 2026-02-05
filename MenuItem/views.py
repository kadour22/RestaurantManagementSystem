from rest_framework.viewsets import ModelViewSet
from .serializers import MenuItemSerializer
from .models import MenuItem

class MenuItemViewSet(ModelViewSet) :
    queryset = MenuItem.objects.select_related('category').all()
    serializer_class = MenuItemSerializer
