from django.db import models
from uuid import uuid4
import os

class Eventos(models.Model):
    titulo = models.CharField("Titulo",max_length=100)
    descripcion = models.TextField("Descripción")
    fecha = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        for imagen in self.imagenes.all():
            imagen.imagen.delete()
        super().delete(*args, **kwargs)
    
class ImagenesEventos(models.Model):
    evento = models.ForeignKey(Eventos, on_delete=models.CASCADE, related_name="imagenes")

    def imagen_ruta(instance, filename):
        ext = filename.split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return os.path.join(f'eventos/{instance.evento.id}/', filename)

    imagen = models.ImageField(upload_to=imagen_ruta)

    class Meta:
        verbose_name = "imagen"
        verbose_name_plural = "imagenes de los eventos"

    def __str__(self):
        return self.evento.titulo