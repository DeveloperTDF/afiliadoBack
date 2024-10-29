from django.db import models

# Create your models here.

class Trabajo(models.Model):
    fecha       =   models.DateField()
    turno       =   models.CharField(max_length=15)
    afiliado    =   models.CharField(max_length=25)
    tarea       =   models.CharField(max_length=25)

    def __str__(self):
        return str(self.tarea)