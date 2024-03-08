from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from . import models


class RegisterForm(UserCreationForm):
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
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError('Um usuário com  este email já existe. ',
                                code='invalid')
            )
        return email


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'classe-a classe-b',
                'placeholder': 'Escreva seu nome aqui',
            }
        ),
        label='Primeiro Nome',
        help_text='Texto de ajuda para seu usuário',
    )

    class Meta:
        model = models.Contact
        fields = (
            'first_name', 'last_name', 'phone',
        )

    def clean(self):
        # cleaned_data = self.cleaned_data

        self.add_error('first_name', ValidationError(
            'Mensagem de erro', code='invalid'))

        self.add_error('last_name', ValidationError(
            'Mensagem de error 2', code='invalid'
        ))
        return super().clean()
