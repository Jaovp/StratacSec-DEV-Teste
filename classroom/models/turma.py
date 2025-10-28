from django.db import models
from .treinamento import Treinamento

class Turma(models.Model):
    treinamento: Treinamento = models.ForeignKey(
        Treinamento,
        on_delete=models.CASCADE,
        related_name='turmas'
    )

    nome: str = models.CharField(max_length=100)
    data_inicio: models.DateField = models.DateField()
    data_conclusao: models.DateField = models.DateField()
    link_acesso: str = models.URLField(max_length=200, blank=True, null=True)

    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    updated_at: models.DateTimeField = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Turma"
        verbose_name_plural = "Turmas"
        ordering = ['data_inicio','nome']

    def __str__(self) -> str:
        return f"{self.nome} - {self.treinamento.nome}"
    
    def clean(self):
        from django.core.exceptions import ValidationError
        if self.data_conclusao < self.data_inicio:
            raise ValidationError("A data de conclusão não pode ser anterior à data de início.")