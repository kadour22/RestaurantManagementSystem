from rest_framework.viewsets import ModelViewSet
from .serializers import restaurant_serializer
from .models import Restaurant

class restaurant_viewset(ModelViewSet) :
    queryset = Restaurant.objects.all()
    serializer_class = restaurant_serializer