from django.db import models
from django.core.validators import RegexValidator, EmailValidator

class Aluno(models.Model):
    nome: str = models.CharField(max_length=100)
    email: str = models.EmailField(
        unique=True,
        validators=[EmailValidator(message="Insira um endereço de email válido.")]
    )
    telefone: str = models.CharField(
        max_length=15,
        blank=True,
        validators=[RegexValidator(
            regex=r'^\+?\d{10,15}$',
            message="O telefone deve conter entre 10 e 15 dígitos"
        )],
    )

    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    updated_at: models.DateTimeField = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Aluno"
        verbose_name_plural = "Alunos"
        ordering = ['nome']

    def __str__(self) -> str:
        return f"{self.nome} ({self.email})"