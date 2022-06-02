from authApp.models.partidos import Partido
from rest_framework import serializers

class MatchResultSerializer(serializers.ModelSerializer):
    equipo_local = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='nombreEquipo'
     )
    
    equipo_visita = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='nombreEquipo'
     )
          
    class Meta:
        model = Partido
        fields = ['equipo_local','equipo_visita', 'marcador_local', 'marcador_visita',
                'fecha_partido']

