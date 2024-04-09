# type: ignore
"""Modulo transmissor de caminhos das views"""
from django.urls import path

from contact import view

app_name = 'contact'

urlpatterns = [
    # main pages
    path('search/', view.search, name='search'),
    path('', view.index, name='index'),

    # contact (CRUD)
    path('contact/<int:contact_id>/read/', view.contact, name='contact'),
    path('contact/create/', view.create, name='create'),
    path('contact/<int:contact_id>/update', view.update, name='update'),
    path('contact/<int:contact_id>/delete', view.delete, name='delete'),
    # user
    path('user/create/', view.register, name='register'),
    path('user/login/', view.login_view, name='login'),
    path('user/logout/', view.logout_view, name='logout'),
]
