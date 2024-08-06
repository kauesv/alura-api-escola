from django.contrib import admin
from escola.models import Estudante, Curso, Matricula


class EstudanteAdmin(admin.ModelAdmin):
    search_fields = ('nome', 'cpf',)
    ordering = ('-criado_em',)
    list_display = (
        'id',
        'nome',
        'cpf',
        'data_nascimento',
        'celular',
        'criado_em',
        'atualizado_em',
        'deletado'
    )
    list_display_links = ('id','nome',)
    list_filter = ('deletado',)
    fields = ('nome', 'cpf', 'data_nascimento', 'celular')
    list_per_page = 20

admin.site.register(Estudante, EstudanteAdmin)

class CursoAdmin(admin.ModelAdmin):
    search_fields = ('codigo',)
    ordering = ('-criado_em',)
    list_display = (
        'id',
        'codigo',
        'descricao',
        'criado_em',
        'atualizado_em',
        'deletado'
    )
    list_display_links = ('id','codigo',)
    list_filter = ('deletado',)
    fields = ('codigo', 'descricao')
    list_per_page = 100

admin.site.register(Curso, CursoAdmin)

class MatriculaAdmin(admin.ModelAdmin):
    search_fields = ('estudante__nome',)
    autocomplete_fields = ['estudante']
    ordering = ('-criado_em',)
    list_display = (
        'id',
        'estudante',
        'curso',
        'periodo',
        'criado_em',
        'atualizado_em',
        'deletado'
    )
    list_display_links = ('id',)
    list_filter = ('deletado', 'periodo',)
    fields = ('estudante', 'curso', 'periodo')
    list_per_page = 100

admin.site.register(Matricula, MatriculaAdmin)