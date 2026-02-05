from django.urls import path
from .views import table_services

urlpatterns = [
    path("tables/", table_services.as_view(), name='tables'),
]