from django.db import models
from .turma import Turma

class Recurso(models.Model):
    class TipoRecurso(models.TextChoices):
        VIDEO = 'video', 'Vídeo'
        PDF = 'pdf', 'Arquivo PDF'
        ZIP = 'zip', 'Arquivo ZIP'

    turma: Turma = models.ForeignKey(
        Turma,
        on_delete=models.CASCADE,
        related_name='recursos'
    )

    tipo_recurso: str = models.CharField(
        max_length=10,
        choices=TipoRecurso.choices
    )

    acesso_previo: bool = models.BooleanField(default=False)
    draft: bool = models.BooleanField(default=True)

    nome: str = models.CharField(max_length=100)
    descricao: str = models.TextField(blank=True, null=True)
    

    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    updated_at: models.DateTimeField = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Recurso"
        verbose_name_plural = "Recursos"
        ordering = ['turma','nome']

    def __str__(self) -> str:
        return f"{self.nome} ({self.get_tipo_recurso_display()})"
    
    def clean(self):
        from django.core.exceptions import ValidationError
        if self.draft and self.acesso_previo:
            raise ValidationError("Um recurso em rascunho não pode ter acesso prévio habilitado.")