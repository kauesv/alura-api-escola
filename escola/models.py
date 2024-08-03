from django.db import models
from .validators import validate_cpf
from core.models import ModelBase


class Estudante(ModelBase):
    nome = models.CharField(max_length = 100)
    email = models.EmailField(blank = False, max_length = 30)
    cpf = models.CharField(max_length=11, null=True, blank=True, validators=[validate_cpf])
    data_nascimento = models.DateField()
    celular = models.CharField(max_length = 14)

    def __str__(self):
        return self.nome

class Curso(ModelBase):
    NIVEL = (
        ('B','Básico'),
        ('I','Intermediário'),
        ('A','Avançado'),
    ) 
    codigo = models.CharField(max_length = 10)
    descricao = models.CharField(max_length = 100, blank = False)
    nivel = models.CharField(max_length = 1, choices = NIVEL, blank = False, null = False, default = 'B')

    def __str__(self):
        return self.codigo

class Matricula(ModelBase):
    PERIODO = (
        ('M','Matutino'),
        ('V','Vespertino'),
        ('N','Noturno'),
    )
    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo = models.CharField(max_length = 1, choices=PERIODO, blank = False, null = False, default="M")

    def __str__(self):
        return f"{self.curso} / {self.estudante}"