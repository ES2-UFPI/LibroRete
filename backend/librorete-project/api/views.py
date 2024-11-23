from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Lista
from .serializers import ListaSerializer

@api_view(['GET'])
def get_listas(request):
    if request.method == 'GET':
        listas = Lista.objects.all()
        serializer = ListaSerializer(listas, many=True)
        return Response(serializer.data)
