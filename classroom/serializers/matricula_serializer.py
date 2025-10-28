from rest_framework import serializers
from classroom.models import Matricula

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = ['id', 'aluno', 'turma', 'data_matricula']
        read_only_fields = ['id', 'data_matricula']

    def validate(self, data):
        aluno = data.get('aluno')
        if Matricula.objects.filter(aluno=aluno).exists():
            raise serializers.ValidationError("O aluno já está matriculado nesta turma.")
        return data
