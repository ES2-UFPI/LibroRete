
from django.test import TestCase
from django.urls import reverse
from api.models import Usuario, Post, Comentario, Interacao, Perfil

class FeedTest(TestCase):
    def setUp(self):
        # Crie um usuário de teste
        self.usuario = Usuario.objects.create(id=777, nome='Raimundo Neto', username='raimundo', email='raimundo@gmail.com', senha='123', foto='foto1')
        self.usuario2 = Perfil.objects.get(id_usuario_perfil= 1)
        self.interacao = Interacao.objects.create(id = 888, tipo = "seguir perfil", id_usuario = self.usuario, id_perfil_seguir = self.usuario2, data_interacao = '2024-12-29 13:00:00')
        self.created_interacao_ids = []

    def tearDown(self):
        # Limpar dados de teste após cada teste
        Interacao.objects.filter(id=self.created_interacao_ids.delete())
        Usuario.objects.filter(id=777).delete()

    def test_get_posts_fedd(self):
        response = self.client.get("api/feed/raimundo/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [{"id":1,"conteudo":"amei esse livro gente :)","midia":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT1ailnDneVDYRN_d55CjsYSy0Vk_sxHyvK9g&s"},{"id":3,"conteudo":"Já tô preparando minha estante kkjjk","midia":"https://static.wixstatic.com/media/c5af93_a56b3ef2ca444a9ba69e260989c10a3c~mv2.jpg/v1/fill/w_980,h_860,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/c5af93_a56b3ef2ca444a9ba69e260989c10a3c~mv2.jpg"},{"id":4,"conteudo":"Lendo um clássicooooo!!!","midia":"https://p2.trrsf.com/image/fget/cf/774/0/images.terra.com/2015/04/17/thumbnail644.jpg"}])

    