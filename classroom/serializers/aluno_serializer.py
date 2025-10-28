from rest_framework import serializers
from classroom.models import  Aluno

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'email', 'telefone', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate_nome(self, value: str) -> str:
        if not value.strip():
            raise serializers.ValidationError("O nome do aluno não pode estar vazio.")
        return value
    
    def validate_email(self, value: str) -> str:
        if not value.strip():
            raise serializers.ValidationError("O e-mail não pode estar vazio.")
        return value