from django.urls import re_path
from .consumers import ordering_consumer
websocket_urlpatterns = [
    re_path(r"^ws/orders/?", ordering_consumer.as_asgi()),
]