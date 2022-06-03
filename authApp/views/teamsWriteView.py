from django.conf import settings
from rest_framework import status, views
from rest_framework_simplejwt.backends import TokenBackend
from authApp.serializers.teamsSerializerWrite import teamsSerializerWrite
from authApp.models.equipos import Equipo
from rest_framework.response import Response

class TeamsWriteView(views.APIView):
    def post(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)
        if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        serializer=teamsSerializerWrite(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("Team created", status=status.HTTP_201_CREATED)