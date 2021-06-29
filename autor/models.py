from django.db import models

# Create your models here.

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    fecha_publicacion = models.DateTimeField()

    def __str__(self):
        return self.nombre
