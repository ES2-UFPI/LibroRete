# from django.test import TestCase
# from django.urls import reverse
# import requests

# class APITests(TestCase):

#     @classmethod
#     def setUpTestData(cls):
#         cls.response = {
#             "user": requests.get(f"http://localhost:8000/api/usuarios/@eduarda"),
#             "perfil": requests.get(f"http://localhost:8000/api/perfis/@eduarda"),
#             "no_perfil": requests.get(f"http://localhost:8000/api/perfis/@marcio"),
#             "listas": requests.get(f"http://localhost:8000/api/listas/@eduarda")
#         }

#     def test_usuario_endpoint(self):
#         self.assertEqual(self.response["user"].status_code, 200)  
#         self.assertEqual(self.response["user"].json(), {"id":1,"nome":"Maria Eduarda","username":"@eduarda","email":"eduarda@gmail.com","senha":"2b869053f31a34090f3a8f14cbc73fb5b9cdde56604379c30a11b9b6f43203a4","foto":"https://png.pngtree.com/png-clipart/20230308/ourlarge/pngtree-cute-cat-sticker-cartoon-kitty-kitten-png-image_6635310.png"})  
    
#     def test_perfil_endpoint_online(self):
#         self.assertEqual(self.response["perfil"].status_code, 200)
    
#     def test_perfil_endpoint_no_user(self):
#         self.assertEqual(self.response["no_perfil"].status_code, 404)

#     def test_perfil_endpoint_numeros(self):
#         self.assertEqual(self.response["perfil"].json()['numero_posts'], 3)
#         self.assertEqual(self.response["perfil"].json()['numero_seguidores'], 3)
#         self.assertEqual(self.response["perfil"].json()['numero_seguindo'], 1)    

#     def test_perfil_endpoint_info_perfil(self):
#         self.assertEqual(self.response["perfil"].json()['bio'], "Idade: 28 anos Profissão: Desenvolvedor de Software | Pronome: Ela/Dela")
#         self.assertEqual(self.response["perfil"].json()['interesses'], "Amante de livros 📚 | Viajante por mundos imaginários e histórias inesquecíveis ✨ | Sempre em busca da próxima página para virar 📖 | Compartilhando paixões literárias e explorando universos através das palavras 🌍📕")  
    
#     def test_perfil_endpoint_info_usuario(self):
#         self.assertEqual(self.response["perfil"].json()['nome'], "Maria Eduarda")
#         self.assertEqual(self.response["perfil"].json()['username'], "@eduarda")
#         self.assertEqual(self.response["perfil"].json()['foto'], "https://png.pngtree.com/png-clipart/20230308/ourlarge/pngtree-cute-cat-sticker-cartoon-kitty-kitten-png-image_6635310.png")
    
#     def test_perfil_endpoint_json(self):
#         self.assertEqual(self.response["perfil"].json(), {"numero_seguidores": 3,"numero_seguindo": 1,"numero_posts": 3,"bio": "Idade: 28 anos Profissão: Desenvolvedor de Software | Pronome: Ela/Dela","nome": "Maria Eduarda","foto": "https://png.pngtree.com/png-clipart/20230308/ourlarge/pngtree-cute-cat-sticker-cartoon-kitty-kitten-png-image_6635310.png","username": "@eduarda","interesses": "Amante de livros 📚 | Viajante por mundos imaginários e histórias inesquecíveis ✨ | Sempre em busca da próxima página para virar 📖 | Compartilhando paixões literárias e explorando universos através das palavras 🌍📕"}) 
    
#     def test_listas_endpoint_online(self):
#         self.assertEqual(self.response["listas"].status_code, 200)
    
#     def test_listas_endpoint_json_original(self):
#         self.assertEqual(self.response["listas"].json()[0]["lista"], "top ever!")
#         self.assertEqual(self.response["listas"].json()[0]["descricao"], "top dos tops")
#         self.assertEqual(self.response["listas"].json()[0]["livros"], [["Carrie, a estranha"],["Hamlet"],["1984"],["Coraline"],["Duna"]])

#         self.assertEqual(self.response["listas"].json()[1]["lista"], "livros de 2024")
#         self.assertEqual(self.response["listas"].json()[1]["descricao"], "meus favoritos de 2024")
#         self.assertEqual(self.response["listas"].json()[1]["livros"], [["Coraline"],["Duna"]])

#         self.assertEqual(self.response["listas"].json()[2]["lista"], "desejados")
#         self.assertEqual(self.response["listas"].json()[2]["descricao"], "minha lista de desejos :)")
#         self.assertEqual(self.response["listas"].json()[2]["livros"], [])
    
#     def test_listas_endpoint_json_api_google(self):
#         self.assertEqual(self.response["listas"].json()[0]["livrosAPIGoogle"][0]["titulo"], "Carrie, a estranha")
#         self.assertEqual(self.response["listas"].json()[0]["livrosAPIGoogle"][0]["autor"], ["Stephen King"])
#         self.assertEqual(self.response["listas"].json()[0]["livrosAPIGoogle"][0]["data_publicacao"], "2007-01-11")
#         self.assertEqual(self.response["listas"].json()[0]["livrosAPIGoogle"][0]["descricao"], "Até 1972, Stephen King ainda era um professor cujo salário mal dava para sustentar a mulher, Tabitha, e os dois filhos. Nas horas vagas, escrevia histórias de suspense, sempre rejeitadas pelas editoras. Foi então que finalizou mais uma obra. Em seguida, porém, desiludido com o mercado editorial, King arremessou-a pela janela. Foi Tabitha quem o convenceu de recuperar os originais e tentar outra vez. Enviado a um editor, o livro foi aceito. Nascia Carrie, a Estranha, obra que lançou Stephen King no cenário literário mundial. O livro narra a atormentada adolescência de uma jovem problemática, perseguida pelos colegas, professores e impedida pela mãe de levar a vida como as garotas de sua idade. Só que Carrie guarda um segredo: quando ela está por perto, objetos voam, portas são trancadas ao sabor do nada, velas se apagam e voltam a iluminar, misteriosamente. Com tantos ingredientes de suspense, Carrie, a Estranha\"\" logo se transformou num enorme sucesso internacional. Ao ser transportado para as telas, em 1976, pelas mãos de Brian de Palma, teve a atriz Sissy Spacek e John Travolta em seus papéis principais.")