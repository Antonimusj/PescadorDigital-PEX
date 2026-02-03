"""
Django settings for projeto_extensionista project.

Arquivo de configurações principais do Django.
"""

from pathlib import Path
import os

# Caminho base do projeto (raiz)
BASE_DIR = Path(__file__).resolve().parent.parent


# ============================
# CONFIGURAÇÕES DE SEGURANÇA
# ============================

# Chave secreta usada para criptografia interna do Django
# (Nunca exponha isso em produção)
SECRET_KEY = "django-insecure-%&y#_q0s3l(y(g1)x#c5&#u9qb(9j(p6pzoo%dd5z@!px2*wlh"

# Debug ligado — NÃO usar em produção
DEBUG = True

# Hosts permitidos a acessar o servidor
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'jessica-unfined-unsplendourously.ngrok-free.dev',
    '192.168.1.6'
]


# ============================
# APLICAÇÕES INSTALADAS
# ============================

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Apps da sua aplicação
    'cadastros',

    # Extensões e dependências
    'crispy_forms',                     # Para formulários estilizados
    'django_cleanup.apps.CleanupConfig', # Remove arquivos antigos automaticamente
    'crispy_bootstrap4',                # Tema Bootstrap 4 para crispy_forms
]


# ============================
# MIDDLEWARES
# ============================

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# Arquivo principal de rotas
ROOT_URLCONF = "projeto_extensionista.urls"


# ============================
# CONFIGURAÇÃO DE TEMPLATES
# ============================

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",

        # Pasta global de templates
        "DIRS": [BASE_DIR / 'templates'],

        # Habilita templates dentro de cada app
        "APP_DIRS": True,

        # Processadores de contexto (variáveis globais nos templates)
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# Aplicação WSGI (para deploy)
WSGI_APPLICATION = "projeto_extensionista.wsgi.application"


# ============================
# BANCO DE DADOS
# ============================



# Tenta conectar ao MySQL para ver se o serviço está ativo

try:
    db_test = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        port=3306,
        connect_timeout=1  # Espera apenas 1 segundo
    )
    db_test.close()

    # Se funcionar, usa o MySQL
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "NAME": "pescadores",
            "USER": "root",
            "PASSWORD": "1234",
            "HOST": "localhost",
            "PORT": "3306",
        }
    }
    print("✅ Conectado ao MySQL com sucesso.")

except Exception:
    # Se falhar, usa o SQLite como plano B
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

    print("⚠️ MySQL não detectado. Usando banco de dados local (SQLite).")


# ============================
# VALIDAÇÃO DE SENHAS
# ============================

AUTH_PASSWORD_VALIDATORS = [
    { "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator" },
    { "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator" },
    { "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator" },
    { "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator" },
]


# ============================
# INTERNACIONALIZAÇÃO
# ============================

LANGUAGE_CODE = "en-us"  # Idioma padrão
TIME_ZONE = "UTC"        # Fuso horário
USE_I18N = True          # Tradução habilitada
USE_TZ = True            # Usa timezone do Django


# ============================
# ARQUIVOS ESTÁTICOS
# ============================

STATIC_URL = '/static/'


# Framework crispy_forms usando template do Bootstrap 4
CRISPY_TEMPLATE_PACK = 'bootstrap4'


# Campo padrão para chaves primárias
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
