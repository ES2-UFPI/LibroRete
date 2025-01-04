from django.test import TestCase
from django.urls import reverse
from api.models import Usuario, Post, Interacao

class PostTestCase(TestCase):

    def test_get_all_posts(self):
        response = self.client.get("/api/posts/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [
    {
        "id": 1,
        "conteudo": "amei esse livro gente :)",
        "midia": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT1ailnDneVDYRN_d55CjsYSy0Vk_sxHyvK9g&s"
    },
    {
        "id": 2,
        "conteudo": "Quem já leu essa maravilha??",
        "midia": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQB_geGRhJccyOA5-XTRH7U1wmae-1CGGaxww&s"
    }
])  # Substitua pelo JSON esperad

