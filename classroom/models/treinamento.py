from django.db import models

class Treinamento(models.Model):
    nome: str = models.CharField(max_length=100)
    descricao: str = models.TextField()

    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    updated_at: models.DateTimeField = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Treinamento"
        verbose_name_plural = "Treinamentos"
        ordering = ['nome']

    def __str__(self) -> str:
        return self.nome