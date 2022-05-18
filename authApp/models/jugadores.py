from django.db import models
from .equipos import Equipo

class Jugador(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre', max_length = 30)
    apellido = models.CharField('Apellido', max_length = 30)
    #fecha_nacimiento = models.DateField()
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, default='Unnasigned')