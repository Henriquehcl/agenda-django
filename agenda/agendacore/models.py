from django.db import models

class compromisso(models.Model):
    #responsavel = models.CharField(max_length=50) # criar um campo para definir quem é o responsável pelo compromisso
    titulo = models.CharField(max_length=50)
    descricao = models.TextField(blank=True, null=True)
    data_compromisso = models.DateTimeField()
    data_criacao = models.DateTimeField(auto_now=True)

"""
após fazer alteração no models, executar comandos
python manage.py makemigrations

"""