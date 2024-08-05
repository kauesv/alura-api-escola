
from django.core.exceptions import ValidationError

def validate_cpf(value):
    """Regras de validação do CPF"""

    #   Limpando o CPF, tirando caracteres
    #cpf = [int(digit) for digit in value if digit.isdigit()]
    cpf = ''.join(filter(str.isdigit, value))

    # Verifica se tem 11 dígitos
    if len(cpf) != 11:
        raise ValidationError('CPF deve ter 11 dígitos.')

    # Verifica números repetidos
    if cpf == cpf[::-1]:
        raise ValidationError('CPF inválido: Todos os dígitos são iguais.')

    # Calcular dígitos verificadores
    cpf = [int(d) for d in cpf]
    soma1 = sum(digit * weight for digit, weight in zip(cpf[:9], range(10, 1, -1)))
    digito1 = (soma1 * 10) % 11
    digito1 = 0 if digito1 == 10 else digito1

    soma2 = sum(digit * weight for digit, weight in zip(cpf[:10], range(11, 1, -1)))
    digito2 = (soma2 * 10) % 11
    digito2 = 0 if digito2 == 10 else digito2

    # Verificar se os dígitos verificadores estão corretos
    if cpf[9] != digito1 or cpf[10] != digito2:
        raise ValidationError('CPF inválido: Dígitos verificadores incorretos.')