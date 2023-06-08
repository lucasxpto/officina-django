from django.contrib import admin

from .models import Cliente, Equipe, Mecanico, Pessoa, Veiculo


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('pessoa',)
    search_fields = ('pessoa__nome',)
    list_filter = ('pessoa__nome',)


@admin.register(Equipe)
class EquipeAdmin(admin.ModelAdmin):
    list_display = ('descricao',)
    search_fields = ('descricao',)
    list_filter = ('descricao',)


@admin.register(Mecanico)
class MecanicoAdmin(admin.ModelAdmin):
    list_display = ('pessoa', 'especialidade')
    search_fields = ('pessoa__nome', 'especialidade')
    list_filter = ('pessoa__nome', 'especialidade')


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco')
    search_fields = ('nome', 'endereco')
    list_filter = ('nome', 'endereco')


@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    list_display = ('placa', 'descricao', 'cliente')
    search_fields = ('placa', 'descricao', 'cliente')
    list_filter = ('placa', 'descricao', 'cliente')
