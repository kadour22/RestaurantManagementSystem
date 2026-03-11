from Restaurant.models import Restaurant
from Restaurant.serializers import restaurant_serializer

class restaurant_service() :
    def get_all_restaurant(self) :
        restaurant = Restaurant.objects.prefetch_related('table').all()
        serializer = restaurant_serializer(restaurant, many=True)
        return serializer.data
    def get_restaurant_by_id(self, id) :
        restaurant = Restaurant.objects.prefetch_related('table').get(id=id)
        serializer = restaurant_serializer(restaurant)
        return serializer.data
    def create_restaurant(self, data) :
        serializer = restaurant_serializer(data=data)
        if serializer.is_valid() :
            serializer.save()
            return serializer.data
        else :
            return serializer.errors
    def update_restaurant(self, id, data) :
        restaurant = Restaurant.objects.get(id=id)
        serializer = restaurant_serializer(restaurant, data=data, partial=True)
        if serializer.is_valid() :
            serializer.save()
            return serializer.data
        else :
            return serializer.errors
    def delete_restaurant(self, id) :
        restaurant = Restaurant.objects.get(id=id)
        restaurant.delete()
        return {"message" : "restaurant deleted successfully"}