import os

import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv(
    dotenv_path='D:\Trabalhos\Analise de Projetos de Sistemas\Projeto_Agenda - teste\Projeto_Agenda\.env')
genai.configure(api_key=os.environ["API_KEY"])


def get_contact_description(description, category):
    prompt = f'''
    Me dê a descrição da personalidade do contato de acordo com os seguintes campos: {description}, {category}.
    Fale de pontos da personalidade que dão oportunidade pra realizar alguma interação com este contato.
    '''

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text
