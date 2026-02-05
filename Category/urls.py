from django.urls import path
from . import views

urlpatterns = [
    path('categorys/', views.category_service.as_view(),name='categorys'),
]