from django.core.exceptions import ValidationError

def validar_cpf(value):
    # Remove pontos e traço do CPF para validar apenas os números
    cpf = value.replace('.', '').replace('-', '')

    # Verifica se tem exatamente 11 dígitos e se todos são números
    if len(cpf) != 11 or not cpf.isdigit():
        raise ValidationError('CPF inválido.')

    # Verifica se todos os dígitos são iguais (casos como 111.111.111-11)
    if cpf == cpf[0] * 11:
        raise ValidationError('CPF inválido.')

    # Cálculo do primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    dig1 = ((soma * 10) % 11) % 10

    # Cálculo do segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    dig2 = ((soma * 10) % 11) % 10

    # Compara os dígitos calculados com os dígitos informados
    if int(cpf[9]) != dig1 or int(cpf[10]) != dig2:
        raise ValidationError('CPF inválido.')
