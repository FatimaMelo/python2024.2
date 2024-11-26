from django.db import models
import hashlib
from django.contrib.auth.hashers import make_password

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=60)
    def __str__(self):
        return self.nome

    telefone = models.CharField(max_length=15)
    def __str__(self):
        return self.telefone

    email = models.CharField(max_length=60)
    def __str__(self):
        return self.email

    senha = models.CharField(max_length=100)

    def set_password(self, senha):
        self.senha = make_password(senha)

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.set_password(self.senha)
        super().save(*args, **kwargs)