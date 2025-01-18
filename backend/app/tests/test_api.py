from django.test import TestCase
from django.urls import reverse
import requests

class APITests(TestCase):
    def test_usuario_endpoint(self):
        response = self.client.get("/api/usuarios/@eduarda")
        
        # Validações
        self.assertEqual(response.status_code, 200)  # Verifica se a resposta é 200 OK
        self.assertEqual(response.json(), {"id":1,"nome":"maria eduarda","username":"@eduarda","email":"eduarda@gmail.com","senha":"2b869053f31a34090f3a8f14cbc73fb5b9cdde56604379c30a11b9b6f43203a4","foto":"https://png.pngtree.com/png-clipart/20230308/ourlarge/pngtree-cute-cat-sticker-cartoon-kitty-kitten-png-image_6635310.png"})  # Substitua pelo JSON esperado
    
    def test_perfil_endpoint_online(self):
        response = self.client.get("/api/perfis/@eduarda")
        self.assertEqual(response.status_code, 200)
    
    def test_perfil_endpoint_numeros(self):
        response = self.client.get("/api/perfis/@eduarda")

        self.assertEqual(response.json()['numero_posts'], 3)
        self.assertEqual(response.json()['numero_seguidores'], 3)
        self.assertEqual(response.json()['numero_seguindo'], 1)    

    def test_perfil_endpoint_info_perfil(self):
        response = self.client.get("/api/perfis/@eduarda")

        self.assertEqual(response.json()['bio'], "Idade: 28 anos Profissão: Desenvolvedor de Software | Pronome: Ela/Dela")
        self.assertEqual(response.json()['interesses'], "Amante de livros 📚 | Viajante por mundos imaginários e histórias inesquecíveis ✨ | Sempre em busca da próxima página para virar 📖 | Compartilhando paixões literárias e explorando universos através das palavras 🌍📕")  
    
    def test_perfil_endpoint_info_usuario(self):
        response = self.client.get("/api/perfis/@eduarda")

        self.assertEqual(response.json()['nome'], "maria eduarda")
        self.assertEqual(response.json()['username'], "@eduarda")
        self.assertEqual(response.json()['foto'], "https://png.pngtree.com/png-clipart/20230308/ourlarge/pngtree-cute-cat-sticker-cartoon-kitty-kitten-png-image_6635310.png")
    
    def test_perfil_endpoint_json(self):
        response = self.client.get("/api/perfis/@eduarda")
        self.assertEqual(response.json(), {"numero_seguidores": 3,"numero_seguindo": 1,"numero_posts": 3,"bio": "Idade: 28 anos Profissão: Desenvolvedor de Software | Pronome: Ela/Dela","nome": "maria eduarda","foto": "https://png.pngtree.com/png-clipart/20230308/ourlarge/pngtree-cute-cat-sticker-cartoon-kitty-kitten-png-image_6635310.png","username": "@eduarda","interesses": "Amante de livros 📚 | Viajante por mundos imaginários e histórias inesquecíveis ✨ | Sempre em busca da próxima página para virar 📖 | Compartilhando paixões literárias e explorando universos através das palavras 🌍📕"}) 
