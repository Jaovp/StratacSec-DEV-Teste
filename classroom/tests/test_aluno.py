from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from classroom.models import Aluno

class AlunoAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            username='admin', email='admin@example.com', password='12345'
        )
        self.client.force_authenticate(user=self.user)
        self.url = '/api/alunos/'

        self.dados_validos = {
            "nome": "João",
            "email": "joao@example.com",
            "telefone": "11999999999"
        }
        self.dados_invalidos = {
            "nome": "",
            "email": "invalido",
        }

    def test_criar_aluno_valido(self):
        response = self.client.post(self.url, self.dados_validos, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_criar_aluno_invalido(self):
        response = self.client.post(self.url, self.dados_invalidos, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_listar_alunos(self):
        Aluno.objects.create(**self.dados_validos)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
