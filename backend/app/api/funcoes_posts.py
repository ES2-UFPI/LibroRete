from . import serializers as srl
from . import models as mdl
from django.utils import timezone

def get_post_interacoes(id_post):
    try:
        post = mdl.Post.objects.get(id=id_post)
        interacoes = mdl.Interacao.objects.filter(id_post=post.id)
        lista_comentarios = []
        #interacoes = mdl.Interacao.objects.filter(id_post=post['id'])
        # quant_curtidas = interacoes.filter(tipo='like post').count()
        # quant_comentarios = interacoes.filter(tipo='criar comentario').count()
        list_comments = interacoes.filter(tipo='criar comentario').values_list('id_comentario', flat=True)
        usuario_id = interacoes.filter(tipo='criar post').values_list('id_usuario', flat=True)[0]
        usuario = mdl.Usuario.objects.get(id=usuario_id)
        for comment in list_comments:
            comentario = mdl.Comentario.objects.get(id=comment)
            serializer_comentario = srl.ComentarioSerializer(comentario)
            comentario = serializer_comentario.data
            usuario_comentario_id = interacoes.filter(id_comentario = comment).values_list('id_usuario', flat=True)[0]
            usuario_comentario = mdl.Usuario.objects.get(id=usuario_comentario_id)
            data = interacoes.filter(id_comentario = comment).values_list('data_interacao', flat=True)[0]
            lista_comentarios.append({
                "id":comentario['id'],
                "conteudo": comentario['conteudo'],
                "nome":  usuario_comentario.username,
                "foto": usuario_comentario.foto,
                "data": data,
                "curtidas": interacoes.filter(tipo='like comentario', id_comentario=comment).count(),
                "quant_respostas": interacoes.filter(tipo='responder comentario', id_comentario_respondido=comment).count(),
                "post_repondido": comentario['id_comentario_pai']
            })    

        data_atual = timezone.now()
        data_post = interacoes.filter(tipo='criar post').values_list('data_interacao', flat=True)[0]
        time_diference = data_atual - data_post
        data = time_diference.total_seconds()/3600


        post= {
            "id": post.id,
            "conteudo": post.conteudo,
            "midia": post.midia,
            "curtidas": interacoes.filter(tipo='like post').count(),
            "comentarios": interacoes.filter(tipo='criar comentario').count(),
            "lista_comentarios": lista_comentarios,
            "time": int(data), 
            "foto": usuario.foto,
            "nome": usuario.username             
        }
        return (post)
    
    except mdl.Post.DoesNotExist:
        return {"erro": "Post não encontrado."}
    except Exception as e:
        return {"erro": f"Erro ao buscar interações: {str(e)}"}