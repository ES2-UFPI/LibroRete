from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from api.models import Usuario, Post, Interacao, Tags, PostTag

class LivroBuscaTests(TestCase):
    def setUp(self):
        self.usuario1 = Usuario.objects.create(id=777, nome='Raimundo Neto', username='@raimundo', email='raimundo@gmail.com', senha='123', foto='foto1')
        self.usuario2 = Usuario.objects.create(id=778, nome='Julio Balestrin', username='@julio', email='julio@gmail.com', senha='456', foto='foto2')

        self.tag1 = Tags.objects.create(nome='#Alienígenas')

        self.post1 = Post.objects.create(id=990, conteudo='OVNIS CONFIRMADOS NOS EUA :o', midia='url1')
        self.post2 = Post.objects.create(id=991, conteudo='Vida em Marte', midia='url2')

        self.post_tag1 = PostTag.objects.create(id_post=self.post1, nome_tag=self.tag1)
        self.post_tag2 = PostTag.objects.create(id_post=self.post2, nome_tag=self.tag1)

        aware_datetime1 = timezone.make_aware(timezone.datetime(2025, 1, 18, 4, 20, 3))
        aware_datetime2 = timezone.make_aware(timezone.datetime(2025, 1, 18, 4, 20, 4))

        self.interacao1 = Interacao.objects.create(id=998, tipo='criar post', data_interacao=aware_datetime1, id_usuario=self.usuario1, id_post=self.post1)
        self.interacao2 = Interacao.objects.create(id=999, tipo='like post', data_interacao=aware_datetime2, id_usuario=self.usuario2, id_post=self.post1)

    def tearDown(self):
        Interacao.objects.filter(id=self.interacao1.id).delete()
        Interacao.objects.filter(id=self.interacao2.id).delete()

        PostTag.objects.filter(id_post=self.post1.id).delete()
        PostTag.objects.filter(id_post=self.post2.id).delete()

        Post.objects.filter(id__in=[self.post1.id, self.post2.id]).delete()

        Tags.objects.filter(nome=self.tag1.nome).delete()

        Usuario.objects.filter(id__in=[self.usuario1.id, self.usuario2.id]).delete()

    def test_get_posts_by_user_top_tags(self):
        response = self.client.get(reverse('posts_recomendados_feed', args=['@raimundo']))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.json()) > 0)
        
        # Verificar se os posts retornados são os esperados
        conteudos = [post['conteudo'] for post in response.json()]
        self.assertIn('Vida em Marte', conteudos)
        self.assertNotIn('OVNIS CONFIRMADOS NOS EUA :o', conteudos)
