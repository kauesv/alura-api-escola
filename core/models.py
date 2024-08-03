from django.db import models


class ModelBase(models.Model):

    class Meta:
        abstract = True

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    deletado = models.BooleanField(default=False, editable=False)


#Estado
#Municipio