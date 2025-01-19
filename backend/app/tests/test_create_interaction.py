# from django.test import TestCase
# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APIClient
# from api.models import Usuario, Post, Comentario, Interacao

# class CreateInteractionTests(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.usuario1 = Usuario.objects.create(id=777, nome='Raimundo Neto', username='raimundo', email='raimundo@gmail.com', senha='123', foto='foto1')
#         self.post1 = Post.objects.create(id=999, conteudo='Post de Teste', midia='url')
#         self.interacoes_criadas = []

#     def tearDown(self):
#         Interacao.objects.filter(id__gt=25).delete()
#         Comentario.objects.filter(id=999).delete()
#         Comentario.objects.filter(id_post=self.post1).delete()
#         Post.objects.filter(id=999).delete()
#         Usuario.objects.filter(id=777).delete()

#     def test_create_interaction_criar_comentario(self):
#         data = {
#             "tipo": "criar comentario",
#             "id_usuario": self.usuario1.id,
#             "id_post": self.post1.id,
#             "conteudo_comentario": "Novo comentário"
#         }
#         response = self.client.post(reverse('criar_interacao'), data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Comentario.objects.count(), 8)
#         self.assertEqual(Comentario.objects.last().conteudo, "Novo comentário")
#         if 'id' in response.data:
#             self.interacoes_criadas.append(response.data['id'])

#     def test_create_interaction_responder_comentario(self):
#         data = {
#             "tipo": "responder comentario",
#             "id_usuario": self.usuario1.id,
#             "id_post": self.post1.id,
#             "id_comentario_pai": 1,
#             "conteudo_comentario": "Resposta ao comentário"
#         }
#         response = self.client.post(reverse('criar_interacao'), data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Comentario.objects.count(), 8)
#         self.assertEqual(Comentario.objects.last().conteudo, "Resposta ao comentário")
#         if 'id' in response.data:
#             self.interacoes_criadas.append(response.data['id'])

#     def test_create_interaction_like_post(self):
#         data = {
#             "tipo": "like post",
#             "id_usuario": self.usuario1.id,
#             "id_post": self.post1.id
#         }
#         response = self.client.post(reverse('criar_interacao'), data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Interacao.objects.count(), 26)
#         self.assertTrue(Interacao.objects.last().curtida)
#         if 'id' in response.data:
#             self.interacoes_criadas.append(response.data['id'])

#     def test_create_interaction_invalid_tipo(self):
#         data = {
#             "tipo": "tipo invalido",
#             "id_usuario": self.usuario1.id,
#             "id_post": self.post1.id
#         }
#         response = self.client.post(reverse('criar_interacao'), data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#         self.assertEqual(response.data["erro"], "Tipo de interação inválido. Tipos válidos: ['criar post', 'criar comentario', 'like post', 'like comentario', 'responder comentario', 'seguir perfil']")

#     def test_create_interaction_usuario_nao_encontrado(self):
#         data = {
#             "tipo": "criar comentario",
#             "id_usuario": 999,
#             "id_post": self.post1.id,
#             "conteudo_comentario": "Comentário"
#         }
#         response = self.client.post(reverse('criar_interacao'), data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
#         self.assertEqual(response.data["erro"], "Usuário não encontrado")

#     def test_create_interaction_post_nao_encontrado(self):
#         data = {
#             "tipo": "criar comentario",
#             "id_usuario": self.usuario1.id,
#             "id_post": 9999,  # Non-existent post ID
#             "conteudo_comentario": "Comentário"
#         }
#         response = self.client.post(reverse('criar_interacao'), data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
#         self.assertEqual(response.data["erro"], "Post não encontrado")