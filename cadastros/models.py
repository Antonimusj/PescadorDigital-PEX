from django.db import models


class Pescadores(models.Model):
    # Opções para o campo situação do defeso
    SITUACAO_CHOICES = [
        ('ativo', 'Ativo'),
        ('inativo', 'Inativo'),
    ]

    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)  # unique=True impede duplicados no banco
    email = models.EmailField(max_length=100, blank=True, null=True)
    celular = models.CharField(max_length=20, blank=True, null=True)
    data_cadastro = models.DateField()

    # Campo que usa o RadioSelect no formulário
    situacao_defeso = models.CharField(
        max_length=10,
        choices=SITUACAO_CHOICES,
        default='ativo'
    )

    def __str__(self):
        return f"{self.nome} ({self.cpf})"