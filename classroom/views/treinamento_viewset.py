from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from classroom.models import Treinamento
from classroom.serializers import TreinamentoSerializer

class TreinamentoViewSet(viewsets.ModelViewSet):
    queryset = Treinamento.objects.all()
    serializer_class = TreinamentoSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()