from django.db import models
from django.contrib.auth.models import User

class Compromisso(models.Model):
    #responsavel = models.CharField(max_length=50) # criar um campo para definir quem é o responsável pelo compromisso
    titulo = models.CharField(max_length=50)
    descricao = models.TextField(blank=True, null=True)
    data_compromisso = models.DateTimeField(verbose_name='Data do Compromisso')
    data_criacao = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    concluido = models.BooleanField(default=False)


    def __str__(self):
        return self.titulo
    
    #formatando padrão da data
    def get_data_compromisso(self):
        return self.data_compromisso.strftime('%d/%m/%Y - %H:%M')

"""
após fazer alteração no models, executar comandos
python manage.py makemigrations
python manage.migrate

"""