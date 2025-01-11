from django.contrib import admin
from .models import Eventos, ImagenesEventos


class ImagenesEventosAdmin(admin.TabularInline):
    model = ImagenesEventos
    extra = 1

class EventosAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha')
    search_fields = ('titulo', 'fecha')
    inlines = [ImagenesEventosAdmin]

admin.site.register(Eventos, EventosAdmin)
admin.site.site_title = "Panel de administración"
admin.site.site_header = "INETERPO ADMIN"
admin.site.index_title = "Bienvenido al panel de administración del INETERPO"