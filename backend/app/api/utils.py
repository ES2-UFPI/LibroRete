from . import serializers as srl
from . import models as mdl


# RETORNA TODAS AS INTERAÇÕES DE UM USUÁRIO
def get_user_interactions(nick):
    try:
        usuario = mdl.Usuario.objects.get(username=nick)
        interacoes = mdl.Interacao.objects.filter(id_usuario=usuario.id)
        serializer = srl.InteracaoSerializer(interacoes, many=True)
    
        return serializer.data
    
    except mdl.Usuario.DoesNotExist:
        return {"erro": "Usuário não encontrado."}
    
    except Exception as e:
        return {"erro": f"Erro ao buscar interações: {str(e)}"}
    

# RETORNA TODOS OS IDS DE POSTS QUE O USUÁRIO INTERAGIU
def get_user_interaction_post_ids(nick):
    try:
        # Obter o usuário pelo username
        usuario = mdl.Usuario.objects.get(username=nick)

        # Obter todas as interações do usuário
        interacoes = mdl.Interacao.objects.filter(id_usuario=usuario.id)

        # Filtrar apenas as interações que possuem um post associado e obter os IDs dos posts
        post_ids = interacoes.filter(id_post__isnull=False).values_list('id_post', flat=True)
        
        return list(post_ids)
    
    except mdl.Usuario.DoesNotExist:
        return {"erro": "Usuário não encontrado."}
    
    except Exception as e:
        return {"erro": f"Erro ao buscar interações: {str(e)}"}

# RETORNA TODOS AS TAGS DE UM DETERMINADO POST
def get_post_tags(post_id):
    try:
        # Get the post
        post = mdl.Post.objects.get(id=post_id)
        
        # Get tags through PostTag relationship
        post_tags = mdl.PostTag.objects.filter(id_post=post)
        
        # Get tag names
        tags = mdl.Tags.objects.filter(
            nome__in=post_tags.values_list('nome_tag', flat=True)
        )
        
        return {
            'tags': [tag.nome for tag in tags]
        }
        
    except mdl.Post.DoesNotExist:
        return {"erro": "Post não encontrado"}
    except Exception as e:
        return {"erro": f"Erro ao buscar tags: {str(e)}"}


def get_user_interaction_tags(username):
    try:
        # Get all post IDs the user interacted with
        post_ids = get_user_interaction_post_ids(username)
        
        # Check if there was an error getting post IDs
        if isinstance(post_ids, dict) and "erro" in post_ids:
            return post_ids
            
        # Get tags for each post
        all_tags = []
        for post_id in post_ids:
            post_tags = get_post_tags(post_id)
            
            # Check if there was an error getting tags
            if isinstance(post_tags, dict) and "erro" in post_tags:
                continue
                
            all_tags.extend(post_tags['tags'])
            
        # Remove duplicates while preserving order
        unique_tags = list(dict.fromkeys(all_tags))
        
        return {
            'tags': unique_tags
        }
        
    except Exception as e:
        return {"erro": f"Erro ao buscar tags: {str(e)}"}


def count_user_tag_interactions(username):
    try:
        usuario = mdl.Usuario.objects.get(username=username)
        interacoes = mdl.Interacao.objects.filter(id_usuario=usuario.id)

        tag_counter = {}
        
        for interacao in interacoes:
            if interacao.id_post:
                post_tags = get_post_tags(interacao.id_post.id)
                
                if isinstance(post_tags, dict) and "tags" in post_tags:
                    for tag in post_tags["tags"]:
                        if tag in tag_counter:
                            tag_counter[tag] += 1
                        else:
                            tag_counter[tag] = 1
        
        sorted_tags = sorted(tag_counter.items(), key=lambda x: x[1], reverse=True)
        
        tag_list = []
        for tag, count in sorted_tags:
            tag_list.append({'tag': tag, 'count': count})

        return {'tag_interactions': tag_list}
        
    except mdl.Usuario.DoesNotExist:
        return {"erro": "Usuário não encontrado"}
    except Exception as e:
        return {"erro": f"Erro ao contar interações: {str(e)}"}
