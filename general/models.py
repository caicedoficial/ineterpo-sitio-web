from django.db import models
from uuid import uuid4
import os

class BaseModel(models.Model):
    titulo = models.CharField("Titulo", max_length=100)
    descripcion = models.TextField("Descripción")
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        for imagen in self.imagenes.all():
            imagen.imagen.delete()
        super().delete(*args, **kwargs)

class Institucional(BaseModel):
    class Meta:
        verbose_name = "Institucional"
        verbose_name_plural = "Institucional"

class Eventos(BaseModel):
    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"

class Implementaciones(BaseModel):
    class Meta:
        verbose_name = "Implementación"
        verbose_name_plural = "Implementaciones"

class BaseImagen(models.Model):
    imagen = models.ImageField(upload_to='')

    class Meta:
        abstract = True

    def imagen_ruta(instance, filename):
        ext = filename.split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return os.path.join(f'{instance._meta.model_name}/{instance.parent.id}/', filename)

class ImagenesInstitucional(BaseImagen):
    institucional = models.ForeignKey(Institucional, on_delete=models.CASCADE, related_name="imagenes")
    imagen = models.ImageField(upload_to=BaseImagen.imagen_ruta)

    class Meta:
        verbose_name = "imagen"
        verbose_name_plural = "imagenes de institucional"

    def __str__(self):
        return self.institucional.titulo

class ImagenesEventos(BaseImagen):
    evento = models.ForeignKey(Eventos, on_delete=models.CASCADE, related_name="imagenes")
    imagen = models.ImageField(upload_to=BaseImagen.imagen_ruta)

    class Meta:
        verbose_name = "imagen"
        verbose_name_plural = "imagenes de eventos"

    def __str__(self):
        return self.evento.titulo

class ImagenesImplementaciones(BaseImagen):
    implementacion = models.ForeignKey(Implementaciones, on_delete=models.CASCADE, related_name="imagenes")
    imagen = models.ImageField(upload_to=BaseImagen.imagen_ruta)

    class Meta:
        verbose_name = "imagen"
        verbose_name_plural = "imagenes de implementaciones"

    def __str__(self):
        return self.implementacion.titulo