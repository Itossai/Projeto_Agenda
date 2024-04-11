"""Arquivo referente a verificação e avaliação de alguns parametros de Contatos
    e categorias"""


def email_validation(user, email):
    """Função que avalia se um email já pertence a um Usuário cadastrado."""
    email_cadastrado = user.objects.filter(email=email).exists()
    return email_cadastrado


def names_verification(first_name, last_name):
    """Função que verifica se o primeiro e segundo nomes são iguais"""
    name_verify = first_name == last_name
    return name_verify


def post_verification(request_method):
    post = "POST"
    verify = request_method == post
    return verify
