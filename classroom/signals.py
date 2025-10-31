from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from classroom.models import Aluno

@receiver(post_save, sender=User)
def criar_aluno_automaticamente(sender, instance, created, **kwargs):
    if created:
        Aluno.objects.create(
            user=instance,
            nome=instance.username,
            email=instance.email
        )
