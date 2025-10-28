from rest_framework import serializers
from classroom.models import Turma

class TurmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turma
        fields = ['id', 'treinamento', 'nome', 'data_inicio', 'data_conclusao', 'link_acesso', 'created_at', 'updated_at']
        read_only_fields = ['id','created_at', 'updated_at']

    def validate(self, data):
        data_inicio = data.get('data_inicio', self.instance.data_inicio if self.instance else None)
        data_conclusao = data.get('data_conclusao', self.instance.data_conclusao if self.instance else None)
        if data_inicio and data_conclusao and data_conclusao < data_inicio:
            raise serializers.ValidationError("A data de conclusão não pode ser anterior à data de início.")
        return data