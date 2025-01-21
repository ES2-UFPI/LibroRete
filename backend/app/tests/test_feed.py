from django.test import TestCase
from django.urls import reverse
from api.models import Usuario, Post, Comentario, Interacao, Perfil

class FeedTest(TestCase):

    def test_get_posts_feed(self):
        response = self.client.get("/api/posts-seguindo/feed/@eduarda")
        self.assertEqual(response.status_code, 200)