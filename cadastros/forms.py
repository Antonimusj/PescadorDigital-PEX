import datetime
from django import forms
from cadastros.models import Pescadores
from django.core.exceptions import ValidationError

from cadastros.validators import validar_cpf


class PescadoresForm(forms.ModelForm):
    # Campo manualmente configurado para garantir o formato DD/MM/AAAA no formulário
    data_cadastro = forms.DateField(
        input_formats=['%d/%m/%Y'],  # Aceita apenas data no formato dia/mês/ano
        initial=datetime.date.today,  # Preenche automaticamente com a data atual
        widget=forms.DateInput(
            format='%d/%m/%Y',
            attrs={
                'class': 'form-control',
                'placeholder': 'DD/MM/AAAA',
                'name': 'data_cadastro'
            }
        )
    )

    class Meta:
        # Modelo usado pelo formulário
        model = Pescadores

        # Campos do modelo que serão exibidos no formulário
        fields = ['nome', 'cpf', 'email', 'celular', 'data_cadastro', 'situacao_defeso']

        # Usando RadioSelect para o campo situacao_defeso
        widgets = {
            'situacao_defeso': forms.RadioSelect,
        }

    # Validação extra para o campo CPF
    def clean_cpf(self):
        # Obtém o CPF enviado pelo usuário
        cpf = self.cleaned_data.get('cpf')

        # Validação personalizada através do arquivo validators.py
        validar_cpf(cpf)

        # Impede cadastro duplicado de CPF
        if Pescadores.objects.filter(cpf=cpf).exists():
            raise ValidationError("Já existe um pescador cadastrado com este CPF.")

        # Retorna o CPF validado
        return cpf
