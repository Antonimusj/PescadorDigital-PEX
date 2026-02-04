@echo off
cd /d %~dp0
call .venv\Scripts\activate

echo ----------------------------------------------
echo   VERIFICANDO SINCRONIZACAO DE DADOS
echo ----------------------------------------------
python sync_db.py

echo ----------------------------------------------
echo   INICIANDO SERVIDOR
echo ----------------------------------------------
start "" "http://127.0.0.1:8000"
python manage.py runserver