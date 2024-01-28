from django.urls import path

from contact import view

app_name = 'contact'

urlpatterns = [
    path('', view.index, name='index'),
]
