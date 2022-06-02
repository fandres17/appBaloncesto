from authApp.models.equipos import Equipo
from rest_framework import serializers

class teamsSerializerWrite(serializers.ModelSerializer):
          
    class Meta:
        model = Equipo
        fields = ['nombreEquipo', 'ciudad', 'correo_electronico']


