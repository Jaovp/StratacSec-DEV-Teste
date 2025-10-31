from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from classroom.models import Turma
from classroom.serializers import TurmaSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

class TurmaPagination(PageNumberPagination):
        page_size = 10

class TurmaViewSet(viewsets.ModelViewSet):
    queryset = Turma.objects.select_related('treinamento').all()
    serializer_class = TurmaSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = TurmaPagination

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()
    
    def get_queryset(self):
        queryset = super().get_queryset()
        treinamento_id = self.request.query_params.get('treinamento')
        if treinamento_id:
            queryset = queryset.filter(treinamento_id=treinamento_id)
        return queryset
    
    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def minhas_turmas(self, request):
        try:
            aluno = request.user.aluno
        except AttributeError:
            return Response({"detail": "Usuário não é um aluno."}, status=400)
        
        turmas = Turma.objects.filter(matriculas__aluno=aluno).select_related('treinamento')

        page = self.paginate_queryset(turmas)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(turmas, many=True)
        return Response(serializer.data)