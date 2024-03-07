from django import forms
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from contact.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            'first_name', 'last_name', 'phone',
        )


def create(request):

    if request.method == 'POST':
        print(request.POST.get('first_name'))
        print(request.POST.get('last_name'))
        print(request.POST.get('phone'))
        context = {
            'form': ContactForm(data=request.POST)
        }
        return render(
            request,
            'contact/create.html',
            context=context
        )
    context = {
        'form': ContactForm()
    }

    return render(
        request,
        'contact/create.html',
        context=context
    )
