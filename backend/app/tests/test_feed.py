from django.test import TestCase
from django.urls import reverse
from api.models import Usuario, Post, Comentario, Interacao, Perfil

class FeedTest(TestCase):

    def test_get_posts_feed(self):
        response = self.client.get("/api/posts-seguindo/feed/@eduarda")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),[{"id":5,"conteudo":"Ler crônicas nunca é demais 😎","midia":"https://m.media-amazon.com/images/I/41pjH50wvrL.jpg","curtidas":1,"comentarios":1,"lista_comentarios":[{"id":6,"conteudo":"Desculpa, mas as únicas crônicas que sei é as de Nárnia kkkk","id_comentario_pai":None,"id_post":5}],"time":304,"foto":"https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/391.png","nome":"@mancini"},{"id":6,"conteudo":"Vou reeler só pela décima vez 😂","midia":"https://cdn.awsli.com.br/800x800/2099/2099388/produto/172329856/3a725c4a7b.jpg","curtidas":0,"comentarios":1,"lista_comentarios":[{"id":7,"conteudo":"Esse eu já perdi as contas de quanto já li","id_comentario_pai":None,"id_post":6}],"time":222,"foto":"https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/391.png","nome":"@mancini"}])
