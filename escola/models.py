from django.utils.translation import gettext_lazy as _  # Marca campos para tradução
from django.core.validators import MinLengthValidator #quantidade minimo de caracteres
from django.db import models
from .validators import validate_cpf
from core.models import ModelBase


class Estudante(ModelBase):

    class Meta:
        verbose_name = _('Estudante')
        verbose_name_plural = _('Estudantes')
        #unique_together = ('cpf',)

    nome = models.CharField(max_length = 100)
    email = models.EmailField(blank = False, max_length = 30)
    cpf = models.CharField(max_length=11, null=True, blank=True, validators=[validate_cpf], unique=True)
    data_nascimento = models.DateField()
    celular = models.CharField(max_length = 14)

    def __str__(self):
        return self.nome

class Curso(ModelBase):

    class Meta:
        verbose_name = _('Curso')
        verbose_name_plural = _('Cursos')
        #unique_together = ('codigo',)

    NIVEL = (
        ('B','Básico'),
        ('I','Intermediário'),
        ('A','Avançado'),
    ) 
    codigo = models.CharField(max_length = 10, unique=True, validators=[MinLengthValidator(3)])
    descricao = models.CharField(max_length = 100, blank = False)
    nivel = models.CharField(max_length = 1, choices = NIVEL, blank = False, null = False, default = 'B')

    def __str__(self):
        return self.codigo

class Matricula(ModelBase):

    class Meta:
        verbose_name = _('Matricula')
        verbose_name_plural = _('Matriculas')

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