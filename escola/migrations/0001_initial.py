# Generated by Django 5.0.3 on 2024-08-03 14:51

import django.db.models.deletion
import escola.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('deletado', models.BooleanField(default=False, editable=False)),
                ('codigo', models.CharField(max_length=10)),
                ('descricao', models.CharField(max_length=100)),
                ('nivel', models.CharField(choices=[('B', 'Básico'), ('I', 'Intermediário'), ('A', 'Avançado')], default='B', max_length=1)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Estudante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('deletado', models.BooleanField(default=False, editable=False)),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=30)),
                ('cpf', models.CharField(blank=True, max_length=11, null=True, validators=[escola.validators.validate_cpf])),
                ('data_nascimento', models.DateField()),
                ('celular', models.CharField(max_length=14)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('deletado', models.BooleanField(default=False, editable=False)),
                ('periodo', models.CharField(choices=[('M', 'Matutino'), ('V', 'Vespertino'), ('N', 'Noturno')], default='M', max_length=1)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escola.curso')),
                ('estudante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escola.estudante')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
