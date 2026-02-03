from django.urls import path
from cadastros import views
from cadastros.views import PescadoresCad, PescadorList, PescadoresEdit, PescadoresDelete

# Mapeamento das URLs da aplicação "cadastros"
urlpatterns = [
    # Página inicial da aplicação
    path("", views.pag_abertura, name="index"),

    # Página para cadastrar pescadores
    path("cadPescadores/", PescadoresCad.as_view(), name="cadPescadores"),

    # Página para listar todos os pescadores
    path("listaPescadores/", PescadorList.as_view(), name="listaPescadores"),

    # Página para editar um pescador específico (usando pk)
    path("editar/<int:pk>/", PescadoresEdit.as_view(), name="editarPescador"),

    # Página para deletar um pescador específico (usando pk)
    path("deletar/<int:pk>/", PescadoresDelete.as_view(), name="deletarPescador"),
]
