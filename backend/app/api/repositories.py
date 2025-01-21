from . import models as mdl

class UsuarioRepository:
    @staticmethod
    def get_by_username(username):
        return mdl.Usuario.objects.get(username=username)

class PostRepository:
    @staticmethod
    def get_by_id(post_id):
        return mdl.Post.objects.get(id=post_id)
    
    @staticmethod
    def get_all():
        return mdl.Post.objects.all()
    
    @staticmethod
    def get_by_query(query):
        return mdl.Post.objects.filter(query).select_related()