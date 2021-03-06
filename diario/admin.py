from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(GrupoCare)
admin.site.register(Mentor)
admin.site.register(Cuidador)

admin.site.register(GrupoCog)
admin.site.register(GrupoAvalia)

admin.site.register(Facilitador)
admin.site.register(Avaliador)

admin.site.register(Participante)
admin.site.register(Nota)
admin.site.register(Partilha)
admin.site.register(Informacoes)
admin.site.register(Respostas)

# Registar dados sobre um grupo
admin.site.register(NotaGrupo)
admin.site.register(PartilhaGrupo)
admin.site.register(Presenca)

# Registar dados sobre uma sessao
admin.site.register(Exercicio)
admin.site.register(Sessao)
