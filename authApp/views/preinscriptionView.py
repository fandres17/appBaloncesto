from rest_framework import status, views
from authApp.serializers.preInscriptionSerializer import PreinscripcionSerializer

from rest_framework.response import Response

class preinscriptionView(views.APIView):
    def post(self, request, *args, **kwargs):
        print("data information")
        print(request.data)
        serializer = PreinscripcionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("Preinscription created", status=status.HTTP_201_CREATED)