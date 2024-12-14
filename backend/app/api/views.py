from rest_framework.response import Response
from rest_framework.decorators import api_view
from . import serializers as srl
from . import models as mdl
from django.db import connection

@api_view(['GET'])
def get_by_nick(request, nick):
#Retorna o perfil do usuário com base no nome de usuário(nickname) 
    try:
        usuario = mdl.Usuario.objects.get(username=nick)
    except:
        return Response({"message": "Usuário não encontrado"}, status=404)
    
    if request.method == 'GET':
        usuario = mdl.Usuario.objects.get(username=nick)
        perfil = mdl.Perfil.objects.get(id_usuario_perfil=usuario.id)
        serializer = srl.PerfilSerializer(perfil)
    return Response(serializer.data)


@api_view(['GET'])
def get_user(request, nick):
    try:
        usuario = mdl.Usuario.objects.get(username=nick)
    except:
        return Response({"message": "Usuário não encontrado"}, status=404)

    if request.method == 'GET':
        usuario = mdl.Usuario.objects.get(username=nick)
        serializer = srl.UsuarioSerializer(usuario)
    return Response(serializer.data)

@api_view(['GET'])
def get_user_lists(request, nick):
    try:
        usuario = mdl.Usuario.objects.get(username=nick)
        perfil = mdl.Perfil.objects.get(id_usuario_perfil=usuario.id)
        
        # Busca todas as listas do usuário
        listas = mdl.Lista.objects.filter(id_perfil_lista=perfil.id)
        
        result = []
        for lista in listas:
            # Pegar instancias de ListaLivro que possuem lista.id
            listalivro = mdl.ListaLivro.objects.filter(id_lista=lista.id)

            # Tabela virtual JOIN de ListaLivro e Livro
            tabela_virtual = listalivro.select_related('isbn_livro')

            # Criar lista apenas com os títulos dos livros
            livros_da_lista = tabela_virtual.values_list('isbn_livro__titulo', flat=True)

            result.append({
                'lista': lista.nome,
                'livros': list(livros_da_lista)
            })
            
        return Response(result)
        
    except mdl.Usuario.DoesNotExist:
        return Response({"message": "Usuário não encontrado"}, status=404)
    except Exception as e:
        return Response({"message": str(e)}, status=500)