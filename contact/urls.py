# type: ignore
# pylint: disable-msg=C0103
"""Modulo transmissor de caminhos das views"""
from django.urls import path

from contact import view

app_name = 'contact'

urlpatterns = ([
    path('', view.index, name='index'),
    path('search/', view.search, name='search'),

    # contact (CRUD)
    path('contact/<int:contact_id>/', view.contact, name='contact'),
    path('contact/create/', view.create, name='create'),
    path('contact/<int:contact_id>/update/', view.update, name='update'),
    path('contact/<int:contact_id>/delete/', view.delete, name='delete'),

    # user
    path('user/create/', view.register, name='register'),
    path('user/login/', view.login_view, name='login'),
    path('user/logout/', view.logout_view, name='logout'),
    path('user/update/', view.user_update, name='user_update'),
])
