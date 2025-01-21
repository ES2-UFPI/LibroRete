from django.test import TestCase
from django.urls import reverse
from api.models import Usuario, Post, Interacao

class PostTestCase(TestCase):

    def test_get_all_posts(self):
        response = self.client.get("/api/posts/")
        self.assertEqual(response.status_code, 200)

    def test_get_post_usuario(self):
        response = self.client.get("/api/posts/@eduarda")
        self.assertEqual(response.status_code, 200)
