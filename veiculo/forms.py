from django import forms

from core.models import Veiculo


class AddVeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = ['placa', 'descricao', 'cliente']
