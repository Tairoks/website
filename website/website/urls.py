
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from website import settings
from django.urls import include
from women.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', index),
    # path('cats/', categories),
    path('', include('women.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = pageNotFound
