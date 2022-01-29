from django.contrib import admin

from agendacore.models import Compromisso


class CompromissoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'usuario', 'data_compromisso', 'data_criacao')
    list_filter = ('usuario', 'data_compromisso')

admin.site.register(Compromisso, CompromissoAdmin)
