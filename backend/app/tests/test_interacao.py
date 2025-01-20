# from django.utils import timezone
# from django.test import TestCase
# from api.models import Usuario, Post, Interacao

# class InteracaoTestCase(TestCase):
#     def setUp(self):
#         # Criar dados de teste antes de cada teste
#         self.usuario = Usuario.objects.create(id=777,username="@Raimundo_Neto",nome="Raimundo",email="rai@test.com",senha="123",foto="url")
#         # data = timezone.localtime(timezone.now()).strftime("%Y-%m-%d %H:%M:%S")
#         data = timezone.now()
#         self.post = Post.objects.create(id=777,conteudo="Post de Teste",data_criacao=data,midia="url")
        
#     def tearDown(self):
#         # Limpar dados de teste após cada teste
#         Interacao.objects.filter(id_usuario=self.usuario).delete()
#         Post.objects.filter(id=777).delete()
#         Usuario.objects.filter(id=777).delete()

#     def test_new_interacao(self):
#         data = {
#             "tipo": "curtir",
#             "id_usuario": self.usuario.id,
#             "id_post": self.post.id
#         }
#         response = self.client.post("/api/interacoes/", data)
#         self.assertEqual(response.status_code, 201)
        
#     def test_interacao_duplicada(self):
#         data = {
#             "tipo": "curtir",
#             "id_usuario": self.usuario.id,
#             "id_post": self.post.id
#         }

#         # Primeira interação
#         self.client.post("/api/interacoes/", data)

#         # Tenta criar a mesma interação
#         response = self.client.post("/api/interacoes/", data)
#         self.assertEqual(response.status_code, 400)

#     def test_interacao_tipo_desconhecido(self):
#         data = {
#             "tipo": "slay it",
#             "id_usuario": self.usuario.id,
#             "id_post": self.post.id
#         }

#         # Tenta mandar interacao
#         response = self.client.post("/api/interacoes/", data)
#         self.assertEqual(response.status_code, 400)

# from django.urls import reverse
# from rest_framework.test import APITestCase
# from api.models import Usuario, Post, Comentario, Interacao

# class InteractionTests(APITestCase):
#     def setUp(self):
#         self.usuario1 = Usuario.objects.create(id=777, nome='Raimundo Neto', username='raimundo', email='raimundo@gmail.com', senha='123', foto='foto1')
#         self.post1 = Post.objects.create(id=999, conteudo='Post de Teste', midia='url')
    
#     def tearDown(self):
#         Interacao.objects.filter(id_usuario=self.usuario1).delete()
#         Post.objects.filter(id=999).delete()
#         Usuario.objects.filter(id=777).delete()

#     def test_create_comment(self):
#         url = reverse('criar_interacao')
#         data = {
#             "tipo": "criar comentario",
#             "id_usuario": self.usuario1.id,
#             "id_post": self.post1.id,
#             "conteudo_comentario": "Queria ta jogando Valheim D;"
#         }
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, 201)
#         self.assertEqual(Comentario.objects.count(), 8)
#         comentario = Comentario.objects.get(id=1)
#         self.assertEqual(comentario.conteudo, "Queria ta jogando Valheim D;")
#         self.assertEqual(comentario.id_post.id, self.post1.id)

#     def test_reply_comment(self):
#         comentario_pai = Comentario.objects.create(id=1, conteudo='Comentário Pai', id_post=self.post1)
#         url = reverse('criar_interacao')
#         data = {
#             "tipo": "responder comentario",
#             "id_usuario": self.usuario1.id,
#             "id_post": self.post1.id,
#             "id_comentario_pai": comentario_pai.id,
#             "conteudo_comentario": "tuudoooo!"
#         }
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, 201)
#         self.assertEqual(Comentario.objects.count(), 9)
#         comentario = Comentario.objects.get(id=2)
#         self.assertEqual(comentario.conteudo, "tuudoooo!")
#         self.assertEqual(comentario.id_post.id, self.post1.id)
#         self.assertEqual(comentario.id_comentario_pai.id, comentario_pai.id)