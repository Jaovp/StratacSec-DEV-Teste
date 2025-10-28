from django.db import models
from .turma import Turma
from .aluno import Aluno

class Matricula(models.Model):
    turma: Turma = models.ForeignKey(
        Turma,
        on_delete=models.CASCADE,
        related_name='matriculas'
    )
    aluno: Aluno = models.ForeignKey(
        Aluno,
        on_delete=models.CASCADE,
        related_name='matriculas'
    )
    data_matricula: models.DateField = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Matrícula"
        verbose_name_plural = "Matrículas"
        unique_together = ('turma', 'aluno') # matricula única 
        ordering = ["-data_matricula"]

    def __str__(self) -> str:
        return f"{self.aluno.nome} matrículado na turma {self.turma.nome}"