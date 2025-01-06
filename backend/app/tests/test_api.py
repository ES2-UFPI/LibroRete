from django.test import TestCase
from django.urls import reverse
import requests

class APITests(TestCase):
    def test_usuario_endpoint(self):
        # Monta a URL completa
        #url = reverse('usuarios', args=['@eduarda'])  # 'usuario_detail' deve ser o nome registrado no seu arquivo de urls.py
        
        # Faz uma requisição GET
        #response = self.client.get(url)
        response = self.client.get("/api/usuarios/@eduarda")
        #response = requests.get('http://localhost:8000/api/usuarios/@eduarda')
        
        # Validações
        self.assertEqual(response.status_code, 200)  # Verifica se a resposta é 200 OK
        self.assertEqual(response.json(), {"id":1,"nome":"maria eduarda","username":"@eduarda","email":"eduarda@gmail.com","senha":"2b869053f31a34090f3a8f14cbc73fb5b9cdde56604379c30a11b9b6f43203a4","foto":"https://png.pngtree.com/png-clipart/20230308/ourlarge/pngtree-cute-cat-sticker-cartoon-kitty-kitten-png-image_6635310.png"})  # Substitua pelo JSON esperado
    
    def test_perfil_endpoint(self):
        response = self.client.get("/api/perfis/@eduarda")
        #response = requests.get('http://localhost:8000/api/perfis/@eduarda')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"id":1,"bio":"Idade: 28 anos Profissão: Desenvolvedor de Software | Pronome: Ela/Dela","interesses":"Amante de livros 📚 | Viajante por mundos imaginários e histórias inesquecíveis ✨ | Sempre em busca da próxima página para virar 📖 | Compartilhando paixões literárias e explorando universos através das palavras 🌍📕","id_usuario_perfil":1})
