from django.db import models

from autor.models import Autor
from editorial.models import Editorial

class Libros(models.Model):
    nombre = models.CharField(max_length=100)
    paginas = models.IntegerField()
    publicado = models.BooleanField()
    fecha_publicacion = models.DateField()
    edicion = models.IntegerField(null=True)
    editorial = models.ForeignKey(
        Editorial,
        on_delete=models.SET_NULL,
        null=True
    )

    autores = models.ManyToManyField(
        Autor,
        related_name='libros'
    )

    def __str__(self):
        return self.nombre
