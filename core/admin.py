from django.contrib import admin, messages

from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.shortcuts import redirect
from django_summernote.admin import SummernoteModelAdmin

from .models import Cliente, Equipe, Mecanico, Pessoa, Veiculo, Servico, Peca, OrdemServico, PecaOrdemServico, QuemSomos


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('pessoa',)
    search_fields = ('pessoa__nome',)


@admin.register(Equipe)
class EquipeAdmin(admin.ModelAdmin):
    list_display = ('descricao',)
    search_fields = ('descricao',)

    def has_add_permission(self, request):
        return request.user.groups.filter(name='gerentes').exists()

    def has_change_permission(self, request, obj=None):
        return request.user.groups.filter(name='gerentes').exists()

    def has_delete_permission(self, request, obj=None):
        return request.user.groups.filter(name='gerentes').exists()


@admin.register(Mecanico)
class MecanicoAdmin(admin.ModelAdmin):
    list_display = ('pessoa', 'especialidade')
    search_fields = ('pessoa__nome', 'especialidade')

    def has_add_permission(self, request):
        return request.user.groups.filter(name='gerentes').exists()

    def has_change_permission(self, request, obj=None):
        return request.user.groups.filter(name='gerentes').exists()

    def has_delete_permission(self, request, obj=None):
        return request.user.groups.filter(name='gerentes').exists()


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


class OSAdminForm(forms.ModelForm):
    veiculo = forms.ModelChoiceField(queryset=Veiculo.objects.all())
    equipe = forms.ModelChoiceField(queryset=Equipe.objects.all())
    servicos = forms.ModelMultipleChoiceField(widget=FilteredSelectMultiple("Serviços", is_stacked=False),
                                              queryset=Servico.objects.all())

    class Meta:
        model = OrdemServico
        fields = ['veiculo', 'equipe', 'servicos']

    def save(self, commit=True):
        os = super().save(commit=False)
        os.veiculo = self.cleaned_data['veiculo']
        os.equipe = self.cleaned_data['equipe']

        if commit:
            os.save()
            self.save_m2m()  # isto salva a relação ManyToMany com servicos

        return os


class OrdemServicoAdmin(admin.ModelAdmin):
    inlines = [PecaOrdemServicoInline, ]
    form = OSAdminForm
    list_display = ('veiculo', 'equipe', 'display_total')
    filter_horizontal = ('servicos',)

    def display_total(self, obj):
        total = 0
        for servico in obj.servicos.all():
            total += servico.preco
        for peca_os in obj.pecaordemservico_set.all():
            total += peca_os.peca.preco * peca_os.quantidade
        return total
    display_total.short_description = 'Total'

class QuemSomosAdmin(SummernoteModelAdmin):
    summernote_fields = ('corpo',)

    def add_view(self, request, form_url='', extra_context=None):
        if QuemSomos.objects.exists():
            messages.set_level(request, messages.ERROR)
            messages.error(request, 'Já existe um objeto QuemSomos. Não é possível criar outro.')
            return redirect("..")
        return super().add_view(request, form_url="", extra_context=extra_context)


admin.site.register(Servico)
admin.site.register(Peca)
admin.site.register(OrdemServico, OrdemServicoAdmin)
admin.site.register(QuemSomos, QuemSomosAdmin)
