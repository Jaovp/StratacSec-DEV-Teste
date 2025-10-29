from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from classroom.models import Treinamento, Turma, Matricula, Aluno
from rest_framework import status

class MatriculaAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(username='admin', password='12345')
        self.client.force_authenticate(user=self.user)

        # Treinamento e Turma base
        self.treinamento = Treinamento.objects.create(nome="Treinamento Y", descricao="Teste Matricula")
        self.turma = Turma.objects.create(
            nome="Turma Y",
            data_inicio="2025-11-05",
            data_conclusao="2025-11-15",
            treinamento=self.treinamento
        )
        self.aluno = Aluno.objects.create(nome='João', email='joao@email.com')

        self.url = '/api/matriculas/'

        # Dados API
        self.dados_validos_api = {
            "aluno": self.aluno.id,  # o próprio usuário
            "turma": self.turma.id
        }
        self.dados_invalidos_api = {
            "aluno": "",
            "turma": ""
        }

        # Dados ORM
        self.dados_validos_model = {
            "aluno": self.aluno,
            "turma": self.turma
        }

    def test_criar_matricula_valida(self):
        response = self.client.post(self.url, self.dados_validos_api)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_criar_matricula_invalida(self):
        response = self.client.post(self.url, self.dados_invalidos_api)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_listar_matriculas(self):
        Matricula.objects.create(**self.dados_validos_model)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detalhar_matricula(self):
        matricula = Matricula.objects.create(**self.dados_validos_model)
        response = self.client.get(f'{self.url}{matricula.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
