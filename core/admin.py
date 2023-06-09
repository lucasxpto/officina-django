from django.contrib import admin

from .models import Cliente, Equipe, Mecanico, Pessoa, Veiculo, Servico, Peca, OrdemServico, PecaOrdemServico


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


class PecaOrdemServicoInline(admin.TabularInline):
    model = PecaOrdemServico
    extra = 1

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        field = super(PecaOrdemServicoInline, self).formfield_for_foreignkey(db_field, request, **kwargs)
        if db_field.name == 'peca':
            # Altera o campo de apresentação de Peça para mostrar a descrição e o preço.
            field.choices = [(peca.id, f"{peca.descricao} - ${peca.preco}") for peca in Peca.objects.all()]
        return field


class OrdemServicoAdmin(admin.ModelAdmin):
    inlines = [PecaOrdemServicoInline, ]
    list_display = ('veiculo',)
    filter_horizontal = ('servicos',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        field = super(OrdemServicoAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
        if db_field.name == 'veiculo':
            # Altera o campo de apresentação de Veículo para mostrar a placa e o nome do cliente.
            field.choices = [(veiculo.id, f"{veiculo.descricao} - {veiculo.placa} - {veiculo.cliente.pessoa.nome}") for
                             veiculo in
                             Veiculo.objects.all()]
        return field

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        field = super(OrdemServicoAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)
        if db_field.name == 'servicos':
            # Altera o campo de apresentação de Serviço para mostrar a descrição e o preço.
            field.choices = [(servico.id, f"{servico.descricao} - ${servico.preco}") for servico in
                             Servico.objects.all()]
        return field


admin.site.register(Servico)
admin.site.register(Peca)
admin.site.register(OrdemServico, OrdemServicoAdmin)
