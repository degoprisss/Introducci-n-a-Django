from django.db import models


class Editorial(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    pagina_web = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
