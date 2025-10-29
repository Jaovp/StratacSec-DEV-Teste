from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from classroom.models import Treinamento, Turma
from rest_framework import status

class TurmaAPITests(APITestCase):
    def setUp(self):
        # Cria usuário e autentica
        self.user = User.objects.create_superuser(username='admin', password='12345')
        self.client.force_authenticate(user=self.user)

        # Cria treinamento base
        self.treinamento = Treinamento.objects.create(
            nome="Treinamento Base",
            descricao="Treinamento para testes de Turma"
        )

        self.url = '/api/turmas/'

        # Dados válidos e inválidos
        self.dados_validos_api = {
            "nome": "Turma A",
            "data_inicio": "2025-11-01",
            "data_conclusao": "2025-11-10",
            "treinamento": self.treinamento.id
        }
        self.dados_invalidos_api = {
            "nome": "",
            "data_inicio": "",
            "data_conclusao": "",
            "treinamento": self.treinamento.id
        }

        # Para criação direta (ORM)
        self.dados_validos_model = {
            "nome": "Turma A",
            "data_inicio": "2025-11-01",
            "data_conclusao": "2025-11-10",
            "treinamento": self.treinamento
        }

    def test_criar_turma_valida(self):
        response = self.client.post(self.url, self.dados_validos_api)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_criar_turma_invalida(self):
        response = self.client.post(self.url, self.dados_invalidos_api)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_listar_turmas(self):
        Turma.objects.create(**self.dados_validos_model)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detalhar_turma(self):
        turma = Turma.objects.create(**self.dados_validos_model)
        response = self.client.get(f'{self.url}{turma.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_atualizar_turma(self):
        turma = Turma.objects.create(**self.dados_validos_model)
        novos_dados = self.dados_validos_api.copy()
        novos_dados["nome"] = "Turma Atualizada"
        response = self.client.put(f'{self.url}{turma.id}/', novos_dados)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_excluir_turma(self):
        turma = Turma.objects.create(**self.dados_validos_model)
        response = self.client.delete(f'{self.url}{turma.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
