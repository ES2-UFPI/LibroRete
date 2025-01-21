from rest_framework.response import Response
from rest_framework.decorators import api_view, parser_classes
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.db.models import Q
from rest_framework.parsers import MultiPartParser, FormParser
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from . import funcoes_tags as u
from . import serializers as srl
from . import models as mdl
from . import funcoes_posts as p
from django.http import HttpRequest
import requests
from abc import ABC, abstractmethod
from .repositories import UsuarioRepository, PostRepository

@api_view(['GET'])
def get_by_nick(request, nick):
    #Retorna o perfil do usuário com base no nome de usuário(nickname) 
    try:
        usuario = UsuarioRepository.get_by_username(nick)
    except mdl.Usuario.DoesNotExist:
        return Response({"message": "Usuário não encontrado"}, status=404)
    
   
    try: 
        perfil = mdl.Perfil.objects.get(id_usuario_perfil=usuario.id)
    except mdl.Perfil.DoesNotExist:
        return Response({"message": "Perfil não encontrado"}, status=404)


    interacoes_numero_seguidores = mdl.Interacao.objects.filter(tipo="seguir perfil", id_perfil_seguir=perfil.id)
    interacoes_numero_seguindo = mdl.Interacao.objects.filter(tipo="seguir perfil", id_usuario=usuario.id)
    interacoes_numero_posts = mdl.Interacao.objects.filter(tipo="criar post", id_usuario=usuario.id)



    return Response({
        "numero_seguidores": interacoes_numero_seguidores.count(),
        "numero_seguindo": interacoes_numero_seguindo.count(),
        "numero_posts": interacoes_numero_posts.count(),
        "bio": perfil.bio,
        "nome": usuario.nome,
        "foto": usuario.foto,
        "username": usuario.username,
        "nome": usuario.nome,
        "interesses": perfil.interesses
    })


@api_view(['GET'])
def get_user(request, nick):
    try:
        usuario = UsuarioRepository.get_by_username(nick)
        serializer = srl.UsuarioSerializer(usuario)
        return Response(serializer.data)
    except:
        return Response({"message": "Usuário não encontrado"}, status=404)


class LivroInfoStrategy(ABC):
    @abstractmethod
    def buscar_info(self, isbn):
        pass

class GoogleBooksInfoStrategy(LivroInfoStrategy):
    def buscar_info(self, isbn):
        try:
            response = requests.get(f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}")
            data = response.json()
        
            book = data["items"][0]
            volume_info = book["volumeInfo"]
            
            return {
                'titulo': volume_info.get("title", "Título não encontrado"),
                'autor': volume_info.get("authors", []),
                'data_publicacao': volume_info.get("publishedDate", "Data não encontrada"),
                'descricao': volume_info.get("description", "Descrição não disponível"),
                'foto': volume_info.get("imageLinks", "Imagem não encontrado")
            }
        except Exception as e:
            return {'error': str(e)}
        

@api_view(['GET'])
def get_user_lists(request, nick):
    try:
        usuario = mdl.Usuario.objects.get(username=nick)
        perfil = mdl.Perfil.objects.get(id_usuario_perfil=usuario.id)
        listas = mdl.Lista.objects.filter(id_perfil_lista=perfil.id)

        livro_info_strategy = GoogleBooksInfoStrategy()
        
        result = []
        for lista in listas:
            listalivro = mdl.ListaLivro.objects.filter(id_lista=lista.id).values_list('isbn_livro')

            array_livros_google_info=[]
            lista_livro=[]
            for isbn in listalivro: 
                livro_info = livro_info_strategy.buscar_info(isbn[0])
                array_livros_google_info.append(livro_info)
                lista_livro.append([livro_info['titulo']])

            result.append({ 
                'lista': lista.nome,
                'descricao': lista.descricao,
                'livros': list(lista_livro),
                'livrosAPIGoogle': array_livros_google_info
            }) 
            
        return Response(result)  
        
    except mdl.Usuario.DoesNotExist:
        return Response({"message": "Usuário não encontrado"}, status=404)
    except Exception as e:
        return Response({"message": str(e)}, status=500)


class InteractionStrategy(ABC):
    @abstractmethod
    def validate(self, data, user):
        pass
    
    @abstractmethod
    def execute(self, data, user):
        pass

class PostLikeStrategy(InteractionStrategy):
    def validate(self, data, user):
        if mdl.Interacao.objects.filter(tipo='like post', id_usuario=data['id_usuario'], id_post=data['id_post']).exists():
            return False, "Usuário já deu like nesse post"
        try:
            post = mdl.Post.objects.get(id=data['id_post'])
        except mdl.Post.DoesNotExist:
            return False, "Post não encontrado"
        return True, {'post': post}

    def execute(self, data, validated_data):
        return {
            'id_post': validated_data['post'],
            'curtida': True
        }

class CommentLikeStrategy(InteractionStrategy):
    def validate(self, data, user):
        # First check if interaction already exists
        if mdl.Interacao.objects.filter(
            id_usuario=data['id_usuario'],
            id_post=data['id_post'],
            id_comentario=data['id_comentario'],
            id_comentario_respondido=data.get('id_comentario_pai')
        ).exists():
            return False, "Usuário já deu like nesse comentário"

        # Then verify if comment exists and belongs to the specified post
        try:
            comentario = mdl.Comentario.objects.get(
                id=data['id_comentario'],
                id_post_id=data['id_post']  # This ensures comment belongs to the post
            )
        except mdl.Comentario.DoesNotExist:
            return False, "Comentário não encontrado ou não pertence ao post especificado"

        return True, {'comentario': comentario}

    def execute(self, data, validated_data):
        return {
            'id_post': validated_data['comentario'].id_post,
            'id_comentario': validated_data['comentario'],
            'curtida': True
        }


class CreateCommentStrategy(InteractionStrategy):
    def validate(self, data, user):
        if not data.get('conteudo_comentario'):
            return False, "Conteúdo do comentário é obrigatório"
        try:
            post = mdl.Post.objects.get(id=data['id_post'])
        except mdl.Post.DoesNotExist:
            return False, "Post não encontrado"
        return True, {'post': post}

    def execute(self, data, validated_data):
        id_coment = mdl.Comentario.objects.count() + 1
        while mdl.Comentario.objects.filter(id=id_coment).exists():
            id_coment += 1

        novo_comentario = mdl.Comentario.objects.create(
            id=id_coment,
            conteudo=data['conteudo_comentario'],
            id_post=validated_data['post']
        )

        # Return only the fields that should be used in Interacao creation
        return {
            'id_comentario': novo_comentario,
            'id_post': validated_data['post'],
            'curtida': False
        }

class ReplyCommentStrategy(InteractionStrategy):
    def validate(self, data, user):
        if not data.get('conteudo_comentario'):
            return False, "Conteúdo do comentário é obrigatório"
        if not data.get('id_comentario_pai'):
            return False, "ID do comentário pai é obrigatório"
        try:
            comentario_pai = mdl.Comentario.objects.get(id=data['id_comentario_pai'])
            post = mdl.Post.objects.get(id=data['id_post'])
        except mdl.Comentario.DoesNotExist:
            return False, "Comentário pai não encontrado"
        except mdl.Post.DoesNotExist:
            return False, "Post não encontrado"
        return True, {'comentario_pai': comentario_pai, 'post': post}

    def execute(self, data, validated_data):
        id_coment = mdl.Comentario.objects.count() + 1
        while mdl.Comentario.objects.filter(id=id_coment).exists():
            id_coment += 1

        novo_comentario = mdl.Comentario.objects.create(
            id=id_coment,
            conteudo=data['conteudo_comentario'],
            id_post=validated_data['post'],
            id_comentario_pai=validated_data['comentario_pai']
        )
        return {
            'id_comentario': novo_comentario,
            'id_post': validated_data['post'],
            'id_comentario_respondido': validated_data['comentario_pai'],
            'curtida': False
        }

class FollowProfileStrategy(InteractionStrategy):
    def validate(self, data, user):
        if mdl.Interacao.objects.filter(
            id_usuario=data['id_usuario'],
            id_perfil_seguir=data['id_perfil_seguir']
        ).exists():
            return False, "Usuário já segue este perfil"
        try:
            perfil = mdl.Perfil.objects.get(id=data['id_perfil_seguir'])
        except mdl.Perfil.DoesNotExist:
            return False, "Perfil a seguir não encontrado"
        return True, {'perfil': perfil}

    def execute(self, data, validated_data):
        return {
            'id_perfil_seguir': validated_data['perfil'],
            'curtida': False
        }

class InteractionContext:
    def __init__(self):
        self._strategies = {
            'like post': PostLikeStrategy(),
            'like comentario': CommentLikeStrategy(),
            'criar comentario': CreateCommentStrategy(),
            'responder comentario': ReplyCommentStrategy(),
            'seguir perfil': FollowProfileStrategy()
        }

    def handle_interaction(self, tipo, data, user):
        if tipo not in self._strategies:
            return False, "Tipo de interação inválido"
        
        strategy = self._strategies[tipo]
        is_valid, result = strategy.validate(data, user)
        if not is_valid:
            return False, result
            
        return True, strategy.execute(data, result)

# {
#     "tipo": "criar comentario",
#     "id_usuario": 4,
#     "id_post": 7,
#     "conteudo_comentario": "Queria ta jogando Valheim D;"
# }
# {
#     "tipo": "responder comentario",
#     "id_usuario": 2,
#     "id_post": 7,
#     "id_comentario_pai": 8,
#     "conteudo_comentario": "tbm ;("
# }
# {
#     "tipo": "like post",
#     "id_usuario": 1,
#     "id_post": 5
# }
# {
#     "tipo": "like comentario",
#     "id_usuario": 2,
#     "id_post": 7,
#     "id_comentario": 8
# }
# {
#     "tipo": "seguir perfil", 
#     "id_usuario": 1,
#     "id_perfil_seguir": 3
# }
@csrf_exempt
@api_view(['POST'])
def create_interaction(request):
    try:
        tipo = request.data.get('tipo')
        id_usuario = request.data.get('id_usuario')

        try:
            usuario = mdl.Usuario.objects.get(id=id_usuario)
        except mdl.Usuario.DoesNotExist:
            return Response({"erro": "Usuário não encontrado"}, status=404)

        interaction_context = InteractionContext()
        success, result = interaction_context.handle_interaction(tipo, request.data, usuario)

        if not success:
            return Response({"erro": result}, status=400)

        id_interacao = mdl.Interacao.objects.count() + 1
        while mdl.Interacao.objects.filter(id=id_interacao).exists():
            id_interacao += 1

        nova_interacao = mdl.Interacao.objects.create(
            id=id_interacao,
            tipo=tipo,
            data_interacao=timezone.now(),
            id_usuario=usuario,
            **result
        )

        serializer = srl.InteracaoSerializer(nova_interacao)
        return Response(serializer.data, status=201)

    except Exception as e:
        return Response({"erro": f"Erro ao criar interação: {str(e)}"}, status=500)


      
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
        posts = PostRepository.get_all()
        posts_list = []
        serializer = srl.PostSerializer(posts, many=True)
        for post in serializer.data:
            posts_list.append(p.get_post_interacoes(post['id']))
        return Response(posts_list, status=200)
    except Exception as e:
        return Response({"erro": f"Erro ao buscar posts: {str(e)}"},status=500)
    

@api_view(['GET'])
def get_post_usuario(request, nick):
    try:
        usuario = UsuarioRepository.get_by_username(nick)
        
        # Filtrar interações do tipo 'criar post' para o usuário
        interacoes = mdl.Interacao.objects.filter(id_usuario=usuario.id, tipo='criar post')
        
        # Serializar os posts relacionados
        posts_user = []
        for interacao in interacoes:
            if interacao.id_post:  # Certificar que a interação possui um post
                post= interacao.id_post  # Já é um objeto Post pela relação ForeignKey
                posts = p.get_post_interacoes(post.id)
                posts_user.append({
                    "id": posts['id'],
                    "conteudo": posts['conteudo'],
                    "midia": posts['midia'],
                    "curtidas": posts['curtidas'],
                    "comentarios": posts['comentarios'],
                    "lista_comentarios": posts['lista_comentarios'],
                    "time": posts['time'],
                })
        
        return Response(posts_user, status=200)
    except mdl.Usuario.DoesNotExist:
        return Response({"erro": "Usuário não encontrado."}, status=404)
    except Exception as e:
        return Response({"erro": f"Erro ao buscar posts: {str(e)}"}, status=500)


@api_view(['GET'])
def get_posts_feed(request, nick):
    try:
        usuario = UsuarioRepository.get_by_username(nick)
        
        # Buscar posts dos usuarios seguidos
        seguindo = mdl.Interacao.objects.filter(id_usuario = usuario.id, tipo = 'seguir perfil')
        posts_feed = []
        for amigo in seguindo:
            perfil_amigo = amigo.id_perfil_seguir
            posts_amigo = mdl.Interacao.objects.filter(id_usuario=perfil_amigo.id_usuario_perfil, tipo = 'criar post')
            for post in posts_amigo:
                serializer = srl.PostSerializer(post.id_post)
                posts = p.get_post_interacoes(serializer.data['id'])
                posts_feed.append(posts)
        
        return Response(posts_feed, status=200)
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
def get_users_by_user_top_tags(request, nick):
    try:
        tag_counts = u.count_user_tag_interactions(nick)
        
        if isinstance(tag_counts, dict) and "erro" in tag_counts:
            return Response(tag_counts, status=404)
        
        top_tags = [tag['tag'] for tag in tag_counts['tag_interactions']]
        
        usuario_atual = mdl.Usuario.objects.get(username=nick)

        users = mdl.Usuario.objects.filter(interacao__id_post__posttag__nome_tag__in=top_tags).exclude(id=usuario_atual.id).distinct()
        
        serializer = srl.UsuarioSerializer(users, many=True)
        
        return Response(serializer.data, status=200)
        
    except mdl.Usuario.DoesNotExist:
        return Response({"erro": "Usuário não encontrado"}, status=404)
    except Exception as e:
        return Response({"erro": f"Erro ao buscar usuários: {str(e)}"}, status=500)
    
    
@api_view(['GET'])
def get_post_tags(request, post_id):
    try:
        post = mdl.Post.objects.get(id=post_id)
        post_tags = mdl.PostTag.objects.filter(id_post=post)
        tags = mdl.Tags.objects.filter(
            nome__in=post_tags.values_list('nome_tag', flat=True)
        )
        return Response({
            'tags': [tag.nome for tag in tags]
        }, status=200)
    except mdl.Post.DoesNotExist:
        return Response({"erro": "Post não encontrado"}, status=404)
    except Exception as e:
        return Response({"erro": f"Erro ao buscar tags: {str(e)}"}, status=500)
    
    
@api_view(['GET'])
def get_user_tags(request, nick):
    try:
        tags = u.get_user_interaction_tags(nick)
        
        if isinstance(tags, dict) and "erro" in tags:
            return Response(tags, status=404)
            
        return Response(tags, status=200)
        
    except Exception as e:
        return Response(
            {"erro": f"Erro ao buscar tags: {str(e)}"}, 
            status=500
        )
    
    
@api_view(['GET'])
def get_user_tag_interactions(request, nick):
    try:
        tag_counts = u.count_user_tag_interactions(nick)
        
        if isinstance(tag_counts, dict) and "erro" in tag_counts:
            return Response(tag_counts, status=404)
            
        return Response(tag_counts, status=200)
        
    except Exception as e:
        return Response(
            {"erro": f"Erro ao buscar contagem de tags: {str(e)}"}, 
            status=500
        )

      
@api_view(['GET'])
def get_posts_by_user_top_tags(request, nick):
    try:
        tag_counts = u.count_user_tag_interactions(nick)

        if isinstance(tag_counts, dict) and "erro" in tag_counts:
            return Response(tag_counts, status=404)

        top_tags = [tag['tag'] for tag in tag_counts['tag_interactions']]

        usuario_atual = mdl.Usuario.objects.get(username=nick)

        # Obter IDs dos posts criados pelo usuário
        posts_criados = mdl.Interacao.objects.filter(
            id_usuario=usuario_atual.id, tipo='criar post'
        ).values_list('id_post', flat=True)

        # Filtrar posts pelas tags e excluir os posts criados pelo usuário
        posts = mdl.Post.objects.filter(
            posttag__nome_tag__in=top_tags
        ).exclude(id__in=posts_criados).distinct()

        serializer = srl.PostSerializer(posts, many=True)

        return Response(serializer.data, status=200)

    except mdl.Usuario.DoesNotExist:
        return Response({"erro": "Usuário não encontrado"}, status=404)
    except Exception as e:
        return Response({"erro": f"Erro ao buscar posts: {str(e)}"}, status=500)

      
@api_view(['GET'])
def combined_feed(request, nick):
    try:
        # Obter posts do feed
        usuario = UsuarioRepository.get_by_username(nick)
        seguindo = mdl.Interacao.objects.filter(id_usuario=usuario.id, tipo='seguir perfil')
        posts_feed = []
        ids_posts =set()
        for amigo in seguindo:
            perfil_amigo = amigo.id_perfil_seguir
            posts_amigo = mdl.Interacao.objects.filter(id_usuario=perfil_amigo.id_usuario_perfil, tipo='criar post')
            for post in posts_amigo:
                posts_feed.append(p.get_post_interacoes(post.id_post.id))
                ids_posts.add(post.id_post.id)


        # Obter posts por top tags
        tag_counts = u.count_user_tag_interactions(nick)
        tag_posts = []
        if isinstance(tag_counts, dict) and "erro" in tag_counts:
            return Response(tag_counts, status=404)
        top_tags = [tag['tag'] for tag in tag_counts['tag_interactions']]
        posts_criados = mdl.Interacao.objects.filter(id_usuario=usuario.id, tipo='criar post').values_list('id_post', flat=True)
        posts_top_tags = mdl.Post.objects.filter(posttag__nome_tag__in=top_tags).exclude(id__in=posts_criados).distinct()
        posts_top_tags = posts_top_tags.exclude(id__in=ids_posts)
        for post in posts_top_tags:
                tag_posts.append(p.get_post_interacoes(post.id))
        # Combinar os resultados
        combined_results = {
            "feed_posts": posts_feed,
            "top_tag_posts": tag_posts
        }

        return Response(combined_results, status=200)

    except mdl.Usuario.DoesNotExist:
        return Response({"erro": "Usuário não encontrado"}, status=404)
    except Exception as e:
        return Response({"erro": f"Erro ao buscar posts: {str(e)}"}, status=500)



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
