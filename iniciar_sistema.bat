@echo off
:: Garante que o script rode na pasta onde ele está localizado
cd /d %~dp0

:: 1. Ativa o ambiente virtual
call .venv\Scripts\activate

:: 2. Abre o navegador na página inicial
start "" "http://127.0.0.1:8000"

:: 3. Inicia o servidor do Django
python manage.py runserver