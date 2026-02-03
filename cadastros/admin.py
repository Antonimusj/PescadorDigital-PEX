from django.contrib import admin
from cadastros.models import Pescadores


# Registra o modelo Pescadores no Django Admin
@admin.register(Pescadores)
class PescadoresAdmin(admin.ModelAdmin):
    # Define quais campos serão exibidos na listagem do admin
    list_display = ("id", "nome", "email", "celular")

    # Define quais campos aparecem dentro do formulário de edição/criação
    fields = ("nome", "email", "celular")
