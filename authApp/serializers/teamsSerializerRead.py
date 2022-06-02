from authApp.models.equipos import Equipo
from rest_framework import serializers

class teamsSerializerRead(serializers.ModelSerializer):

          
    class Meta:
        model = Equipo
        fields = ['id','nombreEquipo', 'ciudad', 'correo_electronico']


