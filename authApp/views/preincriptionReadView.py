
from rest_framework import generics
from authApp.serializers.preInscriptionSerializer import PreinscripcionSerializer
from authApp.models.preinscripcion import Preinscripcion

class PreinscriptionReadListView(generics.ListAPIView):
    serializer_class=PreinscripcionSerializer

#no voy a filtrar nada por ahora TODO: A futuro pensar en sólo traer n preinscripciones
    def get_queryset(self):

        return Preinscripcion.objects.all()