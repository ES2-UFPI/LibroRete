from django.test import TestCase
from django.urls import reverse
from api.models import Usuario

class SearchUsersTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Crie alguns usuários de teste
        cls.usuario1 = Usuario.objects.create(id=777, nome='Raimundo Neto', username='raimundo', email='raimundo@gmail.com', senha='123', foto='foto1')
        cls.usuario2 = Usuario.objects.create(id=778, nome='Julio Balestrin', username='julio', email='julio@gmail.com', senha='456', foto='foto2')

    def test_search_by_nome(self):
        response = self.client.get(reverse('search_users'), {'nome': 'Raimundo'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()['results']), 1)

    def test_search_by_username(self):
        response = self.client.get(reverse('search_users'), {'username': 'julio'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()['results']), 1)

    def test_search_by_nome_and_username(self):
        response = self.client.get(reverse('search_users'), {'nome': 'Raimundo', 'username': 'raimundo'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()['results']), 1)

    def test_search_no_parameters(self):
        response = self.client.get(reverse('search_users'))
        self.assertEqual(response.status_code, 400)

    def test_search_by_email(self):
        response = self.client.get(reverse('search_users'), {'email': 'raimundo@gmail.com'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()['results']), 1)

    def test_search_invalid_nome(self):
        response = self.client.get(reverse('search_users'), {'nome': 'Raimundo123'})
        self.assertEqual(response.status_code, 400)

    def test_search_invalid_username(self):
        response = self.client.get(reverse('search_users'), {'username': 'julio!'})
        self.assertEqual(response.status_code, 400)

    def test_search_invalid_email(self):
        response = self.client.get(reverse('search_users'), {'email': 'invalid-email'})
        self.assertEqual(response.status_code, 400)
