from django.test import TestCase
from django.urls import reverse
from api.models import Usuario, Post, Comentario, Interacao, Perfil

class FeedTest(TestCase):

    def test_get_posts_fedd(self):
        response = self.client.get("/api/posts-seguindo/feed/@eduarda")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['feed_posts'], [
            {
                "id": 5,
                "conteudo": "Ler crônicas nunca é demais 😎",
                "midia": "https://m.media-amazon.com/images/I/41pjH50wvrL.jpg"
            },
            {
                "id": 6,
                "conteudo": "Vou reeler só pela décima vez 😂",
                "midia": "https://cdn.awsli.com.br/800x800/2099/2099388/produto/172329856/3a725c4a7b.jpg"
            }
        ])
