from authApp.models.partidos import Partido
from rest_framework import serializers

class MatchResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partido
        fields = ['equipo_local', 'equipo_visita', 'marcador_local', 'marcador_visita',
                'fecha_partido']

