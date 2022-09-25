import os
import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    nome = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(max_length=255, null=False, blank=False, unique=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ["nome"]


class Local(models.Model):
    def path_imagem(instance, filename):
        ext = filename.split('.')[-1]
        filename = '%s.%s' % (uuid.uuid4(), ext)
        return os.path.join('imagens', filename)

    nome = models.CharField(max_length=255, blank=False, null=False)
    endereco = models.CharField(max_length=255, blank=False, null=False)
    contato = models.CharField(max_length=255, blank=False, null=False)
    descricao = models.CharField(max_length=255, null=True, blank=True)
    imagem_local = models.ImageField(null=True, blank=True, upload_to=path_imagem)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=False, blank=False, related_name="local")

