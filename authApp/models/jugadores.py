from django.db import models
class Jugador(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre', max_length = 30)
    apellido = models.CharField('Apellido', max_length = 30)