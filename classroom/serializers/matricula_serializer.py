from rest_framework import serializers
from classroom.models import Matricula

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = ['id', 'aluno', 'turma', 'data_matricula']
        read_only_fields = ['id', 'data_matricula']

    def validate(self, data):
        aluno = data.get('aluno')
        turma = data.get('turma')
        if Matricula.objects.filter(aluno=aluno, turma=turma).exists():
            raise serializers.ValidationError("O aluno já está matriculado nesta turma.")
        return data
