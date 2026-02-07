from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Restaurant/', include('Restaurant.urls')),
    path('Table/', include('Table.urls')),
    path('Category/', include('Category.urls')),
    path('MenuItem/', include('MenuItem.urls')),
    path('Order/', include('Order.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
