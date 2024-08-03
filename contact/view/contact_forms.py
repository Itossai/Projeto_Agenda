# type: ignore[import-untyped], ignore[syntax]
# type: ignore
"""Impots de módulos do Django
    e da aplicação e verificações"""
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from contact.evalueted import post_verification
from contact.forms import ContactForm
from contact.models import Contact


def create(request):
    """Creando contatos por meio dos formulários"""
    form_action = reverse('contact:create')
    if post_verification(request.method):
        form = ContactForm(data=request.POST)
        context = {
            'form': form,
            'form_action': form_action
        }

        if form.is_valid():
            contact = form.save()
            contact.save()
            return redirect('contact:update', contact_id=contact.pk)
        return render(
            request,
            'contact/create.html',
            context=context
        )
    context = {
        'form': ContactForm(),
        'form_action': form_action
    }

    return render(
        request,
        'contact/create.html',
        context=context
    )


def update(request, contact_id):
    """Atualizando contatos por meio dos formulários"""

    contact = get_object_or_404(Contact, pk=contact_id, show=True)

    form_action = reverse('contact:update', args=(contact_id,))
    if post_verification(request.method):
        form = ContactForm(request.POST, request.FILES, instance=contact)
        context = {
            'form': form,
            'form_action': form_action
        }

        if form.is_valid():
            contact = form.save()
            contact.save()
            return redirect('contact:update', contact_id=contact.pk)
        return render(
            request,
            'contact/create.html',
            context=context
        )
    context = {
        'form': ContactForm(instance=contact),
        'form_action': form_action
    }

    return render(
        request,
        'contact/create.html',
        context=context
    )


def delete(request, contact_id):
    """Creando contatos por meio dos formulários"""
    contact = get_object_or_404(Contact, pk=contact_id, show=True)

    confirmation = request.POST.get('confirmation', 'no')

    if confirmation == 'yes':

        contact.delete()
        return redirect('contact:index')

    return render(request,
                  'contact/contact.html',
                  {
                      'contact': contact,
                      'confirmation': confirmation
                  })
