from rest_framework import serializers
from classroom.models import Recurso

class RecursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recurso
        fields = ['id', 'turma', 'tipo_recurso', 'acesso_previo', 'draft', 'nome', 'descricao', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate(self, data):
        if data.get('acesso_previo') and data.get('draft'):
            raise serializers.ValidationError("Um recurso não pode ser acesso prévio e rascunho ao mesmo tempo.")
        return data