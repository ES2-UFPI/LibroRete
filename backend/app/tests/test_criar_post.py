from django.test import TestCase
from django.urls import reverse
from api.models import Usuario, Post, Comentario

class CreatePostTests(TestCase):
    def setUp(self):
        # Crie um usuário de teste
        self.usuario = Usuario.objects.create(id=777, nome='Raimundo Neto', username='raimundo', email='raimundo@gmail.com', senha='123', foto='foto1')
        self.created_post_ids = []

    def tearDown(self):
        # Limpar dados de teste após cada teste
        Comentario.objects.filter(id_post__in=self.created_post_ids).delete()
        Post.objects.filter(id__in=self.created_post_ids).delete()
        Usuario.objects.filter(id=777).delete()

    def test_create_post_valid_data(self):
        data = {
            'conteudo': 'Entao gente, este eh o novo livro que estou lancando',
            'midia': 'http://example.com/media.jpg',
            'id_usuario': self.usuario.id,
            'data': '2024-12-29 13:00:00'
        }
        response = self.client.post(reverse('criar_post'), data, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        post = Post.objects.get(conteudo='Entao gente, este eh o novo livro que estou lancando')
        self.created_post_ids.append(post.id)
        self.assertEqual(Post.objects.count(), 3)
        self.assertEqual(post.conteudo, 'Entao gente, este eh o novo livro que estou lancando')
        self.assertEqual(post.midia, 'http://example.com/media.jpg')

    def test_create_post_missing_content(self):
        data = {
            'midia': 'http://example.com/media.jpg',
            'id_usuario': self.usuario.id,
            'data': '2024-12-29 13:00:00'
        }
        response = self.client.post(reverse('criar_post'), data, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"erro": "Conteúdo é obrigatório."})

    def test_create_post_invalid_media_url(self):
        data = {
            'conteudo': 'Entao gente, este eh o novo livro que estou lancando',
            'midia': 'invalid-url',
            'id_usuario': self.usuario.id,
            'data': '2024-12-29 13:00:00'
        }
        response = self.client.post(reverse('criar_post'), data, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"erro": "URL da mídia é inválida."})

    def test_create_post_nonexistent_user(self):
        data = {
            'conteudo': 'Entao gente, este eh o novo livro que estou lancando',
            'midia': 'http://example.com/media.jpg',
            'id_usuario': 999,
            'data': '2024-12-29 13:00:00'
        }
        response = self.client.post(reverse('criar_post'), data, content_type='application/json')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {"erro": "Usuário não encontrado."})

    def test_create_post_invalid_date_format(self):
        data = {
            'conteudo': 'Entao gente, este eh o novo livro que estou lancando',
            'midia': 'http://example.com/media.jpg',
            'id_usuario': self.usuario.id,
            'data': 'invalid-date'
        }
        response = self.client.post(reverse('criar_post'), data, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"erro": "Data deve estar no formato '%Y-%m-%d %H:%M:%S'."})

    def test_create_comment_associated_with_post(self):
        while True:
            total_posts = Post.objects.count()
            id_post = total_posts + 1
            if not Post.objects.filter(id=id_post).exists():
                break

        while True:
            total_coment = Comentario.objects.count()
            id_comen = total_coment + 1
            if not Comentario.objects.filter(id=id_comen).exists():
                break

        post = Post.objects.create(
            id=id_post,
            conteudo='Entao gente, este eh o novo livro que estou lancando',
            midia='http://example.com/media.jpg'
        )
        self.created_post_ids.append(post.id)

        comentario = Comentario.objects.create(
            id=id_comen,
            conteudo='Muito ruim, slk',
            id_post=post
        )

        self.assertEqual(Comentario.objects.count(), 6)
        self.assertEqual(comentario.id_post.id, post.id)
