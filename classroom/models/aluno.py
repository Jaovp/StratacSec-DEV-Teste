from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator, EmailValidator
from django.contrib.auth.models import AbstractUser

class Aluno(AbstractUser):
    # O AbstractUser já fornece: username, first_name, last_name, email, password, etc.
    
    telefone = models.CharField(
        max_length=15,
        blank=True,
        validators=[RegexValidator(
            regex=r'^\+?\d{10,15}$',
            message="O telefone deve conter entre 10 e 15 dígitos"
        )],
    )

    email = models.EmailField(
        unique=True,
        max_length=254,
        validators=[EmailValidator(message="Insira um endereço de email válido.")],
    )
    

    class Meta:
        verbose_name = "Usuário (Aluno)"
        verbose_name_plural = "Usuários (Alunos)"
        ordering = ['first_name']

    def __str__(self) -> str:
        return f"{self.first_name} ({self.email})"