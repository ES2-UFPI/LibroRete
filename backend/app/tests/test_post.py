from django.test import TestCase
from django.urls import reverse
from api.models import Usuario, Post, Interacao

class PostTestCase(TestCase):

    def test_get_posts(self):
        response = self.client.get("/api/posts/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [
    {
        "id": 1,
        "conteudo": "amei esse livro gente :)",
        "data_criacao": "2024-12-13T12:13:34Z",
        "midia": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT1ailnDneVDYRN_d55CjsYSy0Vk_sxHyvK9g&s"
    },
    {
        "id": 2,
        "conteudo": "Quem já leu essa maravilha??",
        "data_criacao": "2024-12-14T09:10:17Z",
        "midia": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQB_geGRhJccyOA5-XTRH7U1wmae-1CGGaxww&s"
    }
])  # Substitua pelo JSON esperado

    def test_get_post(self):
        response = self.client.get("/api/posts/1")
        self.assertEqual(response.status_code, 200) 
        self.assertEqual(response.json(), {
    "id": 1,
    "conteudo": "amei esse livro gente :)",
    "data_criacao": "2024-12-13T12:13:34Z",
    "midia": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT1ailnDneVDYRN_d55CjsYSy0Vk_sxHyvK9g&s"
})   
    
    def test_get_post_interacoes(self):
        response = self.client.get("/api/posts/1/interacoes")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [
    {
        "id": 1,
        "tipo": "criar post",
        "data_interacao": "2024-12-13T12:13:34Z",
        "id_usuario": 1,
        "id_post": 1
    }
])  

