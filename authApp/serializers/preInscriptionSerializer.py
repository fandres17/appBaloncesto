from authApp.models.preinscripcion import Preinscripcion
from rest_framework import serializers

class PreinscripcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preinscripcion
        fields = ['nombreEquipo', 'correo_electronico', 'ciudad', 'nombre_encargado',
            'apellido_encargado', 'telefono_encargado']