from django.db import models

class Preinscripcion(models.Model):
    registro_id = models.AutoField(primary_key=True)
    aceptado =models.BooleanField(default=False)
    nombreEquipo = models.CharField('NombreEquipo', max_length = 30)
    correo_electronico = models.EmailField(max_length = 254)
    ciudad = models.CharField('Ciudad', max_length = 30)
    nombre_encargado= models.CharField('NombreEquipo', max_length = 30)
    apellido_encargado= models.CharField('NombreEquipo', max_length = 30)
    telefono_encargado=models.CharField('NombreEquipo', max_length = 30)
    fecha_preinscripcion = models.DateField()

    