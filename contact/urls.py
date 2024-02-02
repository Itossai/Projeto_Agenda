from django.urls import path

from contact import view

app_name = 'contact'

urlpatterns = [
    path('<int:contact_id>/', view.contact, name='contact'),
    path('', view.index, name='index'),  # type: ignore
]
