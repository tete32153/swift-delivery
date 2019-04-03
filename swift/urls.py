
from django.contrib import admin
from django.urls import path
from restaurant.views import index, restaurant
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('restaurant/<int:restaurant_id>/',restaurant, name='details' ),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)