from django.test import TestCase
from django.urls import reverse
from api.models import Livro

class LivroBuscaTests(TestCase):
    def setUp(self):
        # Criação de dados de teste
        self.livro1 = Livro.objects.create(isbn='9999999999990', titulo='O Nome do Vento', autor='Patrick Rothfuss', genero='Fantasia')
        self.livro2 = Livro.objects.create(isbn='9999999999991', titulo='Contato', autor='Carl Sagan', genero='Ficção Científica')
        self.livro3 = Livro.objects.create(isbn='9999999999992', titulo='Admirável Mundo Novo', autor='Aldous Huxley', genero='Distopia')
        
    def tearDown(self):
        # Limpeza dos dados de teste
        Livro.objects.filter(isbn='9999999999990').delete()
        Livro.objects.filter(isbn='9999999999991').delete()
        Livro.objects.filter(isbn='9999999999992').delete()

    def test_busca_por_titulo(self):
        data = {
            'titulo': 'O Nome do Vento'
            }
        response = self.client.get(reverse('api.views.search_books'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.json()) > 0)
        self.assertEqual(response.json()[0]['titulo'], 'O Nome do Vento')

    def test_busca_por_autor(self):
        data = {
            'autor': 'Patrick Rothfuss'
            }
        response = self.client.get(reverse('api.views.search_books'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.json()) > 0)
        self.assertEqual(response.json()[0]['titulo'], 'O Nome do Vento')

    def test_busca_por_genero(self):
        data = {
            'genero': 'Distopia'
            }
        response = self.client.get(reverse('api.views.search_books'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.json()) > 0)
        self.assertEqual(response.json()[0]['titulo'], 'Admirável Mundo Novo')

    def test_busca_com_multiplos_filtros(self):
        data = {
            'titulo': 'Admirável Mundo Novo',
            'autor': 'Aldous Huxley',
            'genero': 'Distopia'
            }
        
        response = self.client.get(reverse('api.views.search_books'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.json()) > 0)
        self.assertEqual(response.json()[0]['titulo'], 'Admirável Mundo Novo')

    def test_busca_sem_parametros(self):
        response = self.client.get(reverse('api.views.search_books'))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"erro": "Pelo menos um parâmetro de busca deve ser fornecido."})

    def test_busca_sem_resultados(self):
        data = {
            'titulo': 'Ovo cozido faz mal?'
            }
        response = self.client.get(reverse('api.views.search_books'), data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {"erro": "Nenhum livro encontrado com os parâmetros fornecidos."})
