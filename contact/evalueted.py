"""Arquivo referente a verificação e avaliação de alguns parametros de Contatos
    e categorias"""


def email_validation(user, email):
    """Função que avalia se um email já pertence a um Usuário cadastrado."""
    email_cadastrado = user.objects.filter(email=email).exists()
    return email_cadastrado
