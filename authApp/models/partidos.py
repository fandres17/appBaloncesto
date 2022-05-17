from django.db import models
from .equipos import Equipo

class Partido(models.Model):
    id_partido = models.AutoField(primary_key=True)
    equipo_local= models.ForeignKey(Equipo, on_delete=models.CASCADE)
    equipo_visita= models.ForeignKey(Equipo, on_delete=models.CASCADE)
    marcador_local= models.IntegerField(default=0)
    marcado_visita= models.IntegerField(default=0)
    fecha_partido =  models.DateTimeField()