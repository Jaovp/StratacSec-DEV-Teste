from rest_framework import serializers
from django.contrib.auth.models import User
from classroom.models import Aluno
from django.db import transaction

class AlunoSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    
    nome = serializers.CharField(source='first_name', required=True) 

    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'email', 'telefone', 'password', 'date_joined', 'last_login']
        read_only_fields = ['id', 'date_joined', 'last_login']

    def validate_nome(self, value: str) -> str:
        if not value.strip():
            raise serializers.ValidationError("O nome não pode estar vazio.")
        return value

    def create(self, validated_data):
        password = validated_data.pop('password')
        nome = validated_data.pop('first_name') 

        # Cria o usuário
        user = Aluno.objects.create_user(
            username=nome, 
            password=password,
            first_name=nome,
            **validated_data
        )
        
        return user