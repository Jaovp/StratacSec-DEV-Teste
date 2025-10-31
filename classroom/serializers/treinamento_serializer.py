from rest_framework import serializers
from classroom.models import Treinamento

class TreinamentoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Treinamento
        fields = ['id', 'nome', 'descricao', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate_nome(self, value: str) -> str:
        if not value.strip():
            raise serializers.ValidationError("O nome do treinamento não pode estar vazio.")
        if Treinamento.objects.filter(nome__iexact=value.strip()).exists():
            raise serializers.ValidationError("Já existe um treinamento com esse nome.")
        return value.strip()