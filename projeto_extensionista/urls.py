"""
URL configuration for DjangoProject1 project.

Arquivo principal de rotas do projeto.
Ele direciona as URLs para outros módulos de views.
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Rota do painel administrativo do Django
    path("admin/", admin.site.urls),

    # Inclui as rotas do app "cadastros"
    # Isso significa que todas as URLs principais serão controladas por cadastros/urls.py
    path('', include('cadastros.urls')),
]
