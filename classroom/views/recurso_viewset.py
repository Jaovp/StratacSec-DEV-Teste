from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from classroom.models import Recurso, Turma
from classroom.serializers import RecursoSerializer
from django.utils import timezone
from rest_framework.decorators import action
from rest_framework.response import Response

class RecursoViewSet(viewsets.ModelViewSet):
    queryset = Recurso.objects.select_related('turma', 'turma__treinamento').all()
    serializer_class = RecursoSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['turma']

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()
    
    def get_queryset(self):
        queryset = super().get_queryset()
        turma_id = self.request.query_params.get('turma')
        if turma_id:
            queryset = queryset.filter(turma_id=turma_id)
        return queryset
    
    @action(detail=True, methods=['get'], url_path='recursos', permission_classes=[IsAuthenticated])
    def recursos_da_turma(self, request, pk=None):
        
        try:
            turma = Turma.objects.get(pk=pk)
        except Turma.DoesNotExist:
            return Response({"detail": "Turma não encontrada."}, status=404)

        # Admin pode ver tudo; alunos só o que têm acesso
        if request.user.is_staff:
            recursos = turma.recursos.all()
        else:
            try:
                aluno = request.user.aluno
            except AttributeError:
                return Response({"detail": "Usuário não é um aluno."}, status=400)

            if not turma.matriculas.filter(aluno=aluno).exists():
                return Response({"detail": "Acesso negado a esta turma."}, status=403)

            hoje = timezone.now().date()
            if hoje < turma.data_inicio:
                recursos = turma.recursos.filter(acesso_previo=True)
            else:
                recursos = turma.recursos.filter(draft=False)

        serializer = self.get_serializer(recursos, many=True)
        return Response(serializer.data)