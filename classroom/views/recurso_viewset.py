from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from classroom.models import Recurso
from classroom.serializers import RecursoSerializer

class RecursoViewSet(viewsets.ModelViewSet):
    queryset = Recurso.objects.select_related('turma').all()
    serializer_class = RecursoSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()