
from rest_framework import generics
from authApp.serializers.matchResultSerializer import MatchResultSerializer
from authApp.models.partidos import Partido

class MatchesResultListView(generics.ListAPIView):
    serializer_class=MatchResultSerializer

#no voy a filtrar nada por ahora TODO: A futuro pensar en sólo traer n partidos
    def get_queryset(self):

        return Partido.objects.all()