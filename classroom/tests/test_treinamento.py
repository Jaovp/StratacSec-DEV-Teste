from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from classroom.models import Treinamento

class TreinamentoAPITests(APITestCase):
    def setUp(self):
    # Cria um superusuário
        self.user = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='12345'
        )
        self.client.force_authenticate(user=self.user)

        self.url = '/api/treinamentos/'

        self.dados_validos = {
            "nome": "Curso de Django",
            "descricao": "Aprenda Django e Django REST Framework"
        }
        self.dados_invalidos = {
            "nome": "",
            "descricao": ""
        }

    # ---- TESTES DE CRIAÇÃO ----
    def test_criar_treinamento_valido(self):
        response = self.client.post(self.url, self.dados_validos, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Treinamento.objects.count(), 1)
        self.assertEqual(Treinamento.objects.get().nome, "Curso de Django")

    def test_criar_treinamento_invalido(self):
        response = self.client.post(self.url, self.dados_invalidos, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # ---- TESTES DE LISTAGEM ----
    def test_listar_treinamentos(self):
        Treinamento.objects.create(**self.dados_validos)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    # ---- TESTES DE DETALHE ----
    def test_detalhar_treinamento(self):
        treino = Treinamento.objects.create(**self.dados_validos)
        response = self.client.get(f'{self.url}{treino.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], "Curso de Django")

    # ---- TESTES DE ATUALIZAÇÃO ----
    def test_atualizar_treinamento(self):
        treino = Treinamento.objects.create(**self.dados_validos)
        novos_dados = {"nome": "Curso Avançado de Django", "descricao": "Atualizado"}
        response = self.client.patch(f'{self.url}{treino.id}/', novos_dados, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        treino.refresh_from_db()
        self.assertEqual(treino.nome, "Curso Avançado de Django")

    # ---- TESTES DE EXCLUSÃO ----
    def test_excluir_treinamento(self):
        treino = Treinamento.objects.create(**self.dados_validos)
        response = self.client.delete(f'{self.url}{treino.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Treinamento.objects.count(), 0)

    # ---- TESTE DE SEGURANÇA ----
    def test_acesso_sem_autenticacao(self):
        self.client.force_authenticate(user=None)  # remove o token
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
