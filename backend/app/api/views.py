from rest_framework.response import Response
from rest_framework.decorators import api_view, parser_classes
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.db.models import Q
from rest_framework.parsers import MultiPartParser, FormParser
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from . import utils as u
from . import serializers as srl
from . import models as mdl


@api_view(['GET'])
def get_by_nick(request, nick):
#Retorna o perfil do usuário com base no nome de usuário(nickname) 
    try:
        usuario = mdl.Usuario.objects.get(username=nick)
    except:
        return Response({"message": "Usuário não encontrado"}, status=404)
    
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


# {
#     "tipo": "curtir",
#     "id_usuario": 777,
#     "id_post": 777
# }
@csrf_exempt # Decorador perigoso?
@api_view(['POST'])
def create_interaction(request):
    try:
        # Obter dados do request
        tipo = request.data.get('tipo')
        id_usuario = request.data.get('id_usuario')
        id_post = request.data.get('id_post')

        # Criando e validando id da nova interacao
        while True:
            total_interacoes = mdl.Interacao.objects.count()
            id_interacao = total_interacoes + 1
            if not mdl.Interacao.objects.filter(id=id_interacao).exists():
                break

        data = timezone.now().strftime("%Y-%m-%d %H:%M:%S")

        # Validar inexistência da interação
        if mdl.Interacao.objects.filter(tipo=tipo,id_usuario=id_usuario,id_post=id_post).exists():
            return Response({"erro": "Interação já existe"}, status=400)

        # Validar tipo de interação
        tipos_validos = ['curtir', 'comentar', 'visualizar']
        if tipo not in tipos_validos:
            return Response({"erro": f"Tipo de interação inválido. Tipos válidos: {tipos_validos}"},status=400)

        # Validar existência do usuário
        try:
            usuario = mdl.Usuario.objects.get(id=id_usuario)
        except mdl.Usuario.DoesNotExist:
            return Response({"erro": "Usuário não encontrado"},status=404)

        # Validar existência do post
        try:
            post = mdl.Post.objects.get(id=id_post)
        except mdl.Post.DoesNotExist:
            return Response({"erro": "Post não encontrado"},status=404)

        # Criar nova interação
        nova_interacao = mdl.Interacao(
            id=id_interacao,
            tipo=tipo,
            data_interacao=data,
            id_usuario=usuario,
            id_post=post
        )
        nova_interacao.save()

        # Serializar e retornar resposta
        serializer = srl.InteracaoSerializer(nova_interacao)
        return Response(serializer.data, status=201)

    except Exception as e:
        return Response({"erro": f"Erro ao criar interação: {str(e)}"},status=500)

# http://localhost:8000/api/buscar-livros/?autor=G&titulo=1
# http://localhost:8000/api/buscar-livros/?autor=G
@api_view(['GET'])
def search_books(request):
    try:
        titulo = request.GET.get('titulo')
        autor = request.GET.get('autor')
        genero = request.GET.get('genero')

        if not titulo and not autor and not genero:
            return Response({"erro": "Pelo menos um parâmetro de busca deve ser fornecido."}, status=400)

        if titulo == "" or autor == "" or genero == "":
            return Response({"erro": "Parâmetros de busca não podem ser vazios."}, status=400)
        
        query = Q()
        if titulo:
            query &= Q(titulo__icontains=titulo)
        if autor:
            query &= Q(autor__icontains=autor)
        if genero:
            query &= Q(genero__iexact=genero)

        livros = mdl.Livro.objects.filter(query).select_related()
        if not livros.exists():
            return Response({"erro": "Nenhum livro encontrado com os parâmetros fornecidos."}, status=404)

        serializer = srl.LivroSerializer(livros, many=True)
        return Response(serializer.data, status=200)
    except Exception as e:
        return Response({"erro": str(e)}, status=500)

@api_view(['GET'])
def get_all_posts(request):
    try:
        posts = mdl.Post.objects.all()
        serializer = srl.PostSerializer(posts, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({"erro": f"Erro ao buscar posts: {str(e)}"},status=500)
    
      
@api_view(['GET'])
def get_post_usuario(request, nick):
    try:
        usuario = mdl.Usuario.objects.get(username=nick)
        
        # Filtrar interações do tipo 'criar post' para o usuário
        interacoes = mdl.Interacao.objects.filter(id_usuario=usuario.id, tipo='criar post')
        
        # Serializar os posts relacionados
        posts_user = []
        for interacao in interacoes:
            if interacao.id_post:  # Certificar que a interação possui um post
                post = interacao.id_post  # Já é um objeto Post pela relação ForeignKey
                serializer = srl.PostSerializer(post)
                posts_user.append(serializer.data)  # Adicionar o JSON do post à lista
        
        return Response(posts_user, status=200)
    except mdl.Usuario.DoesNotExist:
        return Response({"erro": "Usuário não encontrado."}, status=404)
    except Exception as e:
        return Response({"erro": f"Erro ao buscar posts: {str(e)}"}, status=500)

# http://localhost:8000/api/buscar-usuarios/?nome=Maria&username=eduarda
# http://localhost:8000/api/buscar-usuarios/?nome=Mancini&username=mancini
# http://localhost:8000/api/buscar-usuarios/?email=eduarda@gmail.com
# http://localhost:8000/api/buscar-usuarios/?nome=ma
# http://localhost:8000/api/buscar-usuarios/?nome=mA
# %20 para espaço
# %40 para underscore
@api_view(['GET'])
def search_users(request):
    nome = request.GET.get('nome')
    username = request.GET.get('username')
    email = request.GET.get('email')

    if not nome and not username and not email:
        return Response({"error": "Pelo menos um parâmetro de busca deve ser fornecido."}, status=400)

    if nome and not nome.isalpha():
        return Response({"error": "O parâmetro 'nome' deve conter apenas letras."}, status=400)

    if username and not username.isalnum():
        return Response({"error": "O parâmetro 'username' deve conter apenas letras e números."}, status=400)

    if email and ('@' not in email or '.' not in email):
        return Response({"error": "O parâmetro 'email' deve ser um endereço de email válido."}, status=400)

    query = Q()
    if nome:
        query &= Q(nome__icontains=nome)
    if username:
        query &= Q(username__icontains=username)
    if email:
        query &= Q(email__icontains=email)

    users = mdl.Usuario.objects.filter(query).select_related()

    if not users.exists():
        return Response({"message": "Nenhum usuário encontrado com os critérios de busca fornecidos."}, status=404)

    serializer = srl.UsuarioSerializer(users, many=True)
    return Response({
        'results': serializer.data
    })


# {
#    "conteudo": "Este é um novo post",
#    "midia": "http://example.com/media.jpg",
#    "id_usuario": 1
#  }
@csrf_exempt # Decorador perigoso?
@api_view(['POST'])
def create_post(request):
    conteudo = request.data.get('conteudo')
    midia = request.data.get('midia')
    id_usuario = request.data.get('id_usuario')
    data = request.data.get('data')

    while True:
        total_posts = mdl.Post.objects.count()
        id_post = total_posts + 1
        if not mdl.Post.objects.filter(id=id_post).exists():
            break
    
    if not conteudo:
        return Response({"erro": "Conteúdo é obrigatório."}, status=400)

    if not id_usuario:
        return Response({"erro": "ID do usuário é obrigatório."}, status=400)

    try:
        usuario = mdl.Usuario.objects.get(id=id_usuario)
    except mdl.Usuario.DoesNotExist:
        return Response({"erro": "Usuário não encontrado."}, status=404)

    if midia:
        validate = URLValidator()
        try:
            validate(midia)
        except ValidationError:
            return Response({"erro": "URL da mídia é inválida."}, status=400)

    if data:
        try:
            data_criacao = timezone.datetime.strptime(data, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            return Response({"erro": "Data deve estar no formato '%Y-%m-%d %H:%M:%S'."}, status=400)
    else:
        data = timezone.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        novo_post = mdl.Post(
            id=id_post,
            conteudo=conteudo,
            midia=midia
        )
        novo_post.save()
    except Exception as e:
        return Response({"erro": f"Erro ao salvar o post: {str(e)}"}, status=500)

    serializer = srl.PostSerializer(novo_post)
    return Response(serializer.data, status=201)

@api_view(['GET'])
def get_books_by_user_top_tags(request, nick):
    try:
        # Obter todas as tags com as quais o usuário interagiu
        tag_counts = u.count_user_tag_interactions(nick)
        
        if isinstance(tag_counts, dict) and "erro" in tag_counts:
            return Response(tag_counts, status=404)
        
        # Selecionar todas as tags
        all_tags = [tag['tag'][1:] for tag in tag_counts['tag_interactions']]  # Remove o '#'
        
        # Obter todos os gêneros disponíveis
        all_genres = mdl.Livro.objects.values_list('genero', flat=True).distinct()
        
        # Encontrar gêneros correspondentes às tags
        genres = [genre for genre in all_genres if any(genre.lower() in tag.lower() for tag in all_tags)]
        
        # Buscar livros associados aos gêneros selecionados
        books = mdl.Livro.objects.filter(genero__in=genres).distinct()
        
        # Serializar os livros
        serializer = srl.LivroSerializer(books, many=True)
        
        return Response(serializer.data, status=200)
        
    except Exception as e:
        return Response({"erro": f"Erro ao buscar livros: {str(e)}"}, status=500)
