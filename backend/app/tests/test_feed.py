
from django.test import TestCase
from django.urls import reverse
from api.models import Usuario, Post, Comentario, Interacao, Perfil

class FeedTest(TestCase):

    def test_get_posts_fedd(self):
        response = self.client.get("/api/posts/feed/@eduarda")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])

    