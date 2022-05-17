from django.db import models

class Equipo(models.Model):
    id = models.AutoField(primary_key=True)
    nombreEquipo = models.CharField('NombreEquipo', max_length = 30)
    ciudad = models.CharField('Ciudad', max_length = 30)
    correo_electronico = models.EmailField(max_length = 254)