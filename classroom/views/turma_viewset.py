from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from classroom.models import Turma
from classroom.serializers import TurmaSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class TurmaViewSet(viewsets.ModelViewSet):
    queryset = Turma.objects.select_related('treinamento').all()
    serializer_class = TurmaSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()
    
    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def minhas_turmas(self, request):
        try:
            aluno = request.user.aluno
        except AttributeError:
            return Response({"detail": "Usuário não é um aluno."}, status=400)
        
        turmas = Turma.objects.filter(matriculas__aluno=aluno).select_related('treinamento')
        serializer = self.get_serializer(turmas, many=True)
        return Response(serializer.data)