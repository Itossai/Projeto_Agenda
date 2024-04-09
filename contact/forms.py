# type: ignore[import-untyped], ignore[syntax]
# type: ignore
""" Tras o formulário padronizado do Django
    Formulário padrão de Criação de Usuário
    Modelo Padrão de Usuários Django
    Exceção para captura de validação de formulários enviados """
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from . import models
from .evalueted import email_validation


class RegisterForm(UserCreationForm):
    """Formulário para Criação de Usuário na Agenda"""
    first_name = forms.CharField(
        required=True,
        min_length=3
    )
    last_name = forms.CharField(
        required=True,
        min_length=3
    )
    email = forms.EmailField()

    class Meta:
        """Classe Base-Modelo para Criação de Usuário na Agenda"""
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2',
        )

    def clean_email(self):
        """Método utilizado para pegar envio de formulários
            e verificar se o email enviado existe dentro do
            banco de usuários já cadastrados."""
        email = self.cleaned_data.get('email')
        # primeira mudança
        if email_validation(User, email):
            self.add_error(
                'email',
                ValidationError('Um usuário com  este email já existe. ',
                                code='invalid')
            )

        return email


class ContactForm(forms.ModelForm):
    """Formulário para Criação de Contatos na Agenda"""
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'classe-a classe-b',
                'placeholder': 'Escreva seu nome aqui',
            }
        ),
        label='Primeiro Nome',
        help_text='Digite o primeiro nome do Contato',
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'classe-a classe-b',
                'placeholder': 'Escreva seu nome aqui',
            }
        ),
        label='Ultimo Nome',
        help_text='Digite o último nome do Contato',
    )

    class Meta:
        """Classe Base-Modelo para Contatos na Agenda"""
        model = models.Contact
        fields = (
            'first_name', 'last_name', 'phone',
            'email', 'description', 'category',
        )

    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name == last_name:
            msg = ValidationError(
                'Primeiro e Último nomes não podem ser iguais',
                code='invalid')
            self.add_error('first_name', msg)
            self.add_error('last_name', msg)

        return super().clean()
