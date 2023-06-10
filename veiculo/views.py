from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from core.models import Veiculo


class VeiculoListView(ListView):
    model = Veiculo
    template_name = 'veiculo/veiculo_list.html'

    def get_queryset(self):
        queryset = super(VeiculoListView, self).get_queryset()
        return queryset.all()
