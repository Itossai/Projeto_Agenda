# Projeto_Agenda
Projeto para disciplina de APS IFCE
Realizado com framework Django fazendo o interação back/front-end para realização de uma agenda virtual

## Iniciar o Projeto
python -m venv venv
No windows pode ser aberto no cmd e no ps
. venv/bin/activate.bat ou . venv/Scripts/Activate.ps1
pip install django
django-admin startproject project .
python manage.py startapp contact
## Comandos Git de configuração
git config --global user.name 'Seu nome'
git config --global user.email 'seu_email@gmail.com'
git config --global init.defaultBranch main
## Configure o .gitignore
git init
git add .
git commit -m 'Mensagem'
git remote add origin URL_DO_GIT

## Migrando a base de dados DJango
python manage.py makemigrations 
python manage.py migrate

## Criando e modificando a senha de um super usuário Django
python manage.py createsuperuser
python manage.py changepassword USERNAME    