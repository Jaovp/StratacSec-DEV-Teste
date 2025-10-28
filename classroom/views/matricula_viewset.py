from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from classroom.models import Matricula
from classroom.serializers import MatriculaSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.select_related('turma', 'aluno').all()
    serializer_class = MatriculaSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()