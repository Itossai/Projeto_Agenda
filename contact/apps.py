# type: ignore[import-untyped], ignore[syntax]
# type: ignore
"""Importa configuração administrativa do Django"""
from django.apps import AppConfig


class ContactConfig(AppConfig):
    """    Classe Contact em DjangoAdmin
                Acessa os parametros definidos em model de Contact e seus
                respectivos atributors"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'contact'
