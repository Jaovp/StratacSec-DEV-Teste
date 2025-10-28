from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from classroom.models import Recurso, Turma
from classroom.serializers import RecursoSerializer
from django.utils import timezone
from rest_framework.decorators import action
from rest_framework.response import Response

class RecursoViewSet(viewsets.ModelViewSet):
    queryset = Recurso.objects.select_related('turma').all()
    serializer_class = RecursoSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()
    
    @action(detail=False, methods=['get'], url_path='turma/(?P<turma_id>[^/.]+)' , permission_classes=[IsAuthenticated])
    def recursos_turma(self, request, turma_id=None):
        try:
            aluno = request.user.aluno
        except AttributeError:
            return Response({"detail": "Usuário não é um aluno."}, status=400)
        
        try:
            turma = Turma.objects.get(id=turma_id, matriculas__aluno=aluno)
        except Turma.DoesNotExist:
            return Response({"detail": "Turma não encontrada ou acesso negado."}, status=404)
        
        hoje = timezone.now().date()
        if hoje < turma.data_inicio:
            recursos = turma.recursos.filter(acesso_previo=True)
        else:
            recursos = turma.recursos.filter(draft=False)

        serializer = self.get_serializer(recursos, many=True)
        return Response(serializer.data)