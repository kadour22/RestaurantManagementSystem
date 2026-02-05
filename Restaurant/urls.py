from rest_framework.routers import DefaultRouter
from .views import restaurant_viewset

router = DefaultRouter()

router.register('restaurants', restaurant_viewset)

urlpatterns = router.urls