from django.contrib import admin
from django.urls import path, include
from hogar.views import hogar
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", hogar, name="hogar"),
    path("noticias/", include("noticias.urls")),
    path("eventos/", include("eventos.urls")),
    path("__reload__/", include("django_browser_reload.urls")),
]    

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)