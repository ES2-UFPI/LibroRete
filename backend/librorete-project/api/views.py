from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Lista
from .serializers import ListaSerializer
from django.db import connection

@api_view(['GET'])
def get_listas(request):
    if request.method == 'GET':
        listas = Lista.objects.all()
        serializer = ListaSerializer(listas, many=True)
        return Response(serializer.data)
    
def call_procedure(proc_name, params):
    with connection.cursor() as cursor:
        cursor.callproc(proc_name, params)
        results = cursor.fetchall()
        columns = [col[0] for col in cursor.description]
        return [dict(zip(columns, row)) for row in results]

@api_view(['GET'])
def get_user_lists_with_books(request, username):
    listas = call_procedure('busca_listas_de_um_usuario', [username])
    for lista in listas:
        lista['livros'] = call_procedure('busca_livros_por_username', [username])
    return Response(listas)