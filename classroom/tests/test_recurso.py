from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from classroom.models import Treinamento, Turma, Recurso
from rest_framework import status

class RecursoAPITests(APITestCase):
    def setUp(self):
        # Usuário e autenticação
        self.user = User.objects.create_superuser(username='admin', password='12345')
        self.client.force_authenticate(user=self.user)

        # Cria Turma base
        self.treinamento = Treinamento.objects.create(nome="Treinamento X", descricao="Teste Recurso")
        self.turma = Turma.objects.create(
            nome="Turma X",
            data_inicio="2025-11-01",
            data_conclusao="2025-11-10",
            treinamento=self.treinamento
        )

        self.url = '/api/recursos/'

        # Dados para API (IDs)
        self.dados_validos_api = {
            "turma": self.turma.id,
            "tipo_recurso": "video",
            "acesso_previo": False,
            "draft": True,
            "nome": "Introdução ao Django",
            "descricao": "Vídeo explicativo sobre os conceitos iniciais de Django"
        }
        self.dados_invalidos_api = {
            "nome": "",
            "descricao": "",
            "turma": self.turma.id,
            "tipo_recurso": "audio",
            "acesso_previo": True,
            "draft": True,
            "descricao": ""
        }

        # Dados para ORM
        self.dados_validos_model = {
            "nome": "Projetor",
            "descricao": "Projetor multimídia",
            "turma": self.turma
        }

    def test_criar_recurso_valido(self):
        response = self.client.post(self.url, self.dados_validos_api)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_criar_recurso_invalido(self):
        response = self.client.post(self.url, self.dados_invalidos_api)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_listar_recursos(self):
        Recurso.objects.create(**self.dados_validos_model)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detalhar_recurso(self):
        recurso = Recurso.objects.create(**self.dados_validos_model)
        response = self.client.get(f'{self.url}{recurso.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
