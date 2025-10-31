from rest_framework import serializers
from classroom.models import Recurso

class RecursoSerializer(serializers.ModelSerializer):
    turma_nome = serializers.CharField(source='turma.nome', read_only=True)
    treinamento_nome = serializers.CharField(source='turma.treinamento.nome', read_only=True)

    class Meta:
        model = Recurso
        fields = ['id', 'turma', 'tipo_recurso', 'acesso_previo', 'draft', 'nome', 'descricao', 'turma_nome', 'treinamento_nome', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at', 'turma_nome', 'treinamento_nome']

    def validate(self, data):
        acesso_previo = data.get('acesso_previo', getattr(self.instance, 'acesso_previo', False))
        draft = data.get('draft', getattr(self.instance, 'draft', False))
        if acesso_previo and draft:
            raise serializers.ValidationError("Um recurso em rascunho não pode ter acesso prévio habilitado.")
        return data