from django.db import models

# Create your models here.
class Afiliado (models.Model):
    fecha       =   models.DateField()
    nombre      =   models.CharField(max_length=20)
    direccion   =   models.CharField(max_length=20)
    telefono    =   models.CharField(max_length=10)

    def __str__(self):
        return str(self.nombre)