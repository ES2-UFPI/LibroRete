'''
from django.utils import timezone
from django.test import TestCase
from django.urls import reverse
from api.models import Usuario, Post, Interacao

class InteracaoTestCase(TestCase):
    def setUp(self):
        # Criar dados de teste antes de cada teste
        self.usuario = Usuario.objects.create(id=777,username="@Raimundo_Neto",nome="Raimundo",email="rai@test.com",senha="123",foto="url")
        #data = timezone.localtime(timezone.now()).strftime("%Y-%m-%d %H:%M:%S")
        data = timezone.now()
        self.post = Post.objects.create(id=777,conteudo="Post de Teste",data_criacao=data,midia="url")
        
    def tearDown(self):
        # Limpar dados de teste após cada teste
        Interacao.objects.filter(id_usuario=self.usuario).delete()
        Post.objects.filter(id=777).delete()
        Usuario.objects.filter(id=777).delete()

    def test_new_interacao(self):
        data = {
            "tipo": "curtir",
            "id_usuario": self.usuario.id,
            "id_post": self.post.id
        }
        response = self.client.post("/api/interacoes/", data)
        self.assertEqual(response.status_code, 201)
        
    def test_interacao_duplicada(self):
        data = {
            "tipo": "curtir",
            "id_usuario": self.usuario.id,
            "id_post": self.post.id
        }

        # Primeira interação
        self.client.post("/api/interacoes/", data)

        # Tenta criar a mesma interação
        response = self.client.post("/api/interacoes/", data)
        self.assertEqual(response.status_code, 400)

    def test_interacao_tipo_desconhecido(self):
        data = {
            "tipo": "slay it",
            "id_usuario": self.usuario.id,
            "id_post": self.post.id
        }

        # Tenta mandar interacao
        response = self.client.post("/api/interacoes/", data)
        self.assertEqual(response.status_code, 400)
'''