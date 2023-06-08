from django.contrib import admin

from .models import Cliente, Equipe, Mecanico, Pessoa, Veiculo, OS, Item


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('pessoa',)
    search_fields = ('pessoa__nome',)


@admin.register(Equipe)
class EquipeAdmin(admin.ModelAdmin):
    list_display = ('descricao',)
    search_fields = ('descricao',)


@admin.register(Mecanico)
class MecanicoAdmin(admin.ModelAdmin):
    list_display = ('pessoa', 'especialidade')
    search_fields = ('pessoa__nome', 'especialidade')


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco')
    search_fields = ('nome', 'endereco')


@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    list_display = ('placa', 'descricao',)
    search_fields = ('placa', 'descricao',)


# class ItemInline(admin.TabularInline):
#     model = Item
#     extra = 0

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'valor')
    search_fields = ('descricao', 'valor')


@admin.register(OS)
class OSAdmin(admin.ModelAdmin):
    list_display = ('data_entrega', 'data_emissao', 'veiculo', 'equipe')
