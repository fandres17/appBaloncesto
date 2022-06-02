
from rest_framework import generics
from authApp.serializers.teamsSerializerRead import teamsSerializerRead
from authApp.models.equipos import Equipo

class TeamsListView(generics.ListAPIView):
    serializer_class=teamsSerializerRead

#no voy a filtrar nada por ahora TODO: A futuro pensar en sólo traer n equipos
    def get_queryset(self):

        return Equipo.objects.all()