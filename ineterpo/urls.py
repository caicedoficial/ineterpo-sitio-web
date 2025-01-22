from django.contrib import admin
from django.urls import path, include
from hogar.views import hogar
from django.conf import settings
from django.conf.urls.static import static
from general import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", hogar, name="hogar"),
    path("noticias/", include("noticias.urls")),
    path("eventos/", views.eventos, name="eventos"),
    path("implementaciones/", views.implementaciones, name="implementaciones"),
    path("institucional/", views.institucional, name="institucional"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)