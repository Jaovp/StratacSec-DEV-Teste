from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from classroom.models import Turma
from classroom.serializers import TurmaSerializer

class TurmaViewSet(viewsets.ModelViewSet):
    queryset = Turma.objects.select_related('treinamento').all()
    serializer_class = TurmaSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()