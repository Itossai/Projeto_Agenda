# type: ignore[import-untyped], ignore[syntax]
# type: ignore
""" Verificador de autenticação de Usuário
    Modelo Padrão do Django
    Define zona de tempo padrão do Django"""

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.
# id (primary key - automático)
# first_name (string), last_name (string), phone (string)
# email (email), created_date (date), description (text)
# category (foreign key), show (boolean), picture (imagem)

# Depois
# owner (foreign key)


class Category(models.Model):
    """Modelo Padrão de Categoria, um atributo composto de um Contato"""

    class Meta:
        """Faz com que Categoria seja definida com um outro nome
            Ao invés de usar o nome 'Category' utiliar Categoria"""
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.name}'


class Contact(models.Model):

    """Modelo Contatos do sistema de contatos do app"""

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    created_date = models.DateField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL,
                              blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
