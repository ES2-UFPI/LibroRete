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
    },
    {
        "id": 3,
        "conteudo": "Já tô preparando minha estante kkjjk",
        "midia": "https://static.wixstatic.com/media/c5af93_a56b3ef2ca444a9ba69e260989c10a3c~mv2.jpg/v1/fill/w_980,h_860,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/c5af93_a56b3ef2ca444a9ba69e260989c10a3c~mv2.jpg"
    },
    {
        "id": 4,
        "conteudo": "Lendo um clássicooooo!!!",
        "midia": "https://p2.trrsf.com/image/fget/cf/774/0/images.terra.com/2015/04/17/thumbnail644.jpg"
    },
    {
        "id": 5,
        "conteudo": "Ler crônicas nunca é demais 😎",
        "midia": "https://m.media-amazon.com/images/I/41pjH50wvrL.jpg"
    },
    {
        "id": 6,
        "conteudo": "Vou reeler só pela décima vez 😂",
        "midia": "https://cdn.awsli.com.br/800x800/2099/2099388/produto/172329856/3a725c4a7b.jpg"
    },
    {
        "id": 7,
        "conteudo": "Aprendendo mais sobre um dos meus países favoritos <3",
        "midia": "https://m.media-amazon.com/images/I/91NDFlRPGTL._UF894,1000_QL80_.jpg"
    },
    {
        "id": 8,
        "conteudo": "Será se as cores são tão importantes assim? 🤔 Veremos 👀",
        "midia": "https://m.media-amazon.com/images/I/41RuWuRzqsL._SY445_SX342_.jpg"
    }
])  # Substitua pelo JSON esperado

    def test_get_post_usuario(self):

        response = self.client.get("/api/posts/@eduarda")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"feed_posts":[{"id":5,"conteudo":"Ler crônicas nunca é demais 😎","midia":"https://m.media-amazon.com/images/I/41pjH50wvrL.jpg","curtidas":1,"comentarios":1,"lista_comentarios":[{"id":6,"conteudo":"Desculpa, mas as únicas crônicas que sei é as de Nárnia kkkk","id_comentario_pai":null,"id_post":5}],"time":304,"foto":"https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/391.png","nome":"@mancini"},{"id":6,"conteudo":"Vou reeler só pela décima vez 😂","midia":"https://cdn.awsli.com.br/800x800/2099/2099388/produto/172329856/3a725c4a7b.jpg","curtidas":0,"comentarios":1,"lista_comentarios":[{"id":7,"conteudo":"Esse eu já perdi as contas de quanto já li","id_comentario_pai":null,"id_post":6}],"time":221,"foto":"https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/391.png","nome":"@mancini"}],"top_tag_posts":[{"id":5,"conteudo":"Ler crônicas nunca é demais 😎","midia":"https://m.media-amazon.com/images/I/41pjH50wvrL.jpg","curtidas":1,"comentarios":1,"lista_comentarios":[{"id":6,"conteudo":"Desculpa, mas as únicas crônicas que sei é as de Nárnia kkkk","id_comentario_pai":null,"id_post":5}],"time":304,"foto":"https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/391.png","nome":"@mancini"},{"id":7,"conteudo":"Aprendendo mais sobre um dos meus países favoritos <3","midia":"https://m.media-amazon.com/images/I/91NDFlRPGTL._UF894,1000_QL80_.jpg","curtidas":1,"comentarios":0,"lista_comentarios":[],"time":251,"foto":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTb0Zcycgq7wKymbe-jMm8Jadi6-_c6sc0WBA&s","nome":"@ygor"}]})
