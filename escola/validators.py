
from django.core.exceptions import ValidationError
from validate_docbr import CPF
import re

def validate_nome(value):
    """Regras de validação do nome"""
    if not value.isalpha():
        raise ValidationError('O campo nome só pode ter letras!')

def validate_celular(value):
    """Regras de validação de celular"""
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, value)
    if not resposta:
        raise ValidationError('O campo celular deve seguir o modelo: 11 90000-0000')

def validate_cpf(value):
    """Regras de validação do CPF"""

    #   Limpando o CPF, tirando caracteres
    numero_cpf = ''.join(filter(str.isdigit, value))

    # Verifica se tem 11 dígitos
    if len(numero_cpf) != 11:
        raise ValidationError('O campo CPF deve ter 11 dígitos!')

    # Calcular dígitos verificadores
    cpf = CPF()
    if not cpf.validate(numero_cpf):
        raise ValidationError('CPF inválido, dígitos incorretos.')