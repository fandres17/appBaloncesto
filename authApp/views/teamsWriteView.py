from rest_framework import status, views
from authApp.serializers.teamsSerializerWrite import teamsSerializerWrite
from authApp.models.equipos import Equipo
from rest_framework.response import Response

class TeamsWriteView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer=teamsSerializerWrite(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("Team created", status=status.HTTP_201_CREATED)