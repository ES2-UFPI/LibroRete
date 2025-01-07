from rest_framework import serializers
from . import models as mdl


class UsuarioSerializer(serializers.ModelSerializer): 
  class Meta: 
    model = mdl.Usuario 
    fields = '__all__' # Inclui todos os campos da tabela

class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = mdl.Perfil
        fields = '__all__'

class InteracaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = mdl.Interacao
        fields = ['id', 'tipo', 'data_interacao', 'id_usuario', 'id_post']


class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = mdl.Livro
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = mdl.Post
        fields = '__all__'
