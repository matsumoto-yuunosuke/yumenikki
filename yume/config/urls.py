from django.conf.urls.static import static
from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("yumenikki.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.IMAGE_URL, document_root=settings.IMAGE_ROOT)
