from rest_framework import status, views
from authApp.serializers import preInscriptionSerializer
from rest_framework.response import Response

class preinscriptionView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = preInscriptionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("Preinscription created", status=status.HTTP_201_CREATED)