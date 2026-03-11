from rest_framework.views import APIView
from rest_framework.filters import SearchFilter, OrderingFilter
from .services import restaurant_service

class restaurant_viewset(APIView) :

    def __init__(self, *args, **kwargs) :
        super().__init__(*args, **kwargs)
        self.restaurant_service = restaurant_service()
    
    def list(self, request) :
        return self.restaurant_service.get_all_restaurant()
    
    def retrieve(self, request, id) :
        return self.restaurant_service.get_restaurant_by_id(id)
    
    def create(self, request) :
        return self.restaurant_service.create_restaurant(request.data)