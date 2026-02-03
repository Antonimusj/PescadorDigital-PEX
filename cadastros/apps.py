from django.apps import AppConfig


# Configuração da aplicação "cadastros"
class CadastrosConfig(AppConfig):
    # Define o tipo padrão de campo para chaves primárias (BigAutoField = inteiro grande e autoincrementado)
    default_auto_field = "django.db.models.BigAutoField"

    # Nome da aplicação que o Django usa internamente
    name = "cadastros"
