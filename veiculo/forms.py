from django import forms

from core.models import Veiculo


class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = ['placa', 'descricao']
