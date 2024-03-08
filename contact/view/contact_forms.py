
from django.shortcuts import render

from contact.forms import ContactForm


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
