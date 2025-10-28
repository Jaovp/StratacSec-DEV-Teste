from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'treinamentos', views.TreinamentoViewSet, basename='treinamento')
router.register(r'turmas', views.TurmaViewSet, basename='turma')
router.register(r'matriculas', views.MatriculaViewSet, basename='matricula')
router.register(r'recursos', views.RecursoViewSet, basename='recurso')
router.register(r'alunos', views.AlunoViewSet, basename='aluno')

urlpatterns = [
    path('api/', include(router.urls)),
]
