from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.models import Veiculo
from veiculo.forms import AddVeiculoForm


class VeiculoListView(LoginRequiredMixin, ListView):
    model = Veiculo
    template_name = 'veiculo/veiculo_list.html'

    def get_queryset(self):
        queryset = super(VeiculoListView, self).get_queryset()
        return queryset.all()


class VeiculoCreateView(LoginRequiredMixin, CreateView):
    model = Veiculo
    form_class = AddVeiculoForm
    template_name = 'veiculo/veiculo_form.html'

    def form_valid(self, form):
        veiculo = form.save(commit=False)
        veiculo.save()
        messages.success(self.request, 'Veículo cadastrado com sucesso.')
        return redirect('veiculos:listar')

    def form_invalid(self, form):
        messages.error(self.request, 'Erro ao cadastrar veículo.')
        print(form.errors)
        return super().form_invalid(form)


class VeiculoUpdateView(LoginRequiredMixin, UpdateView):
    model = Veiculo
    form_class = AddVeiculoForm
    template_name = 'veiculo/veiculo_form.html'

    def get_success_url(self):
        return reverse_lazy('veiculos:listar')

    def form_valid(self, form):
        messages.success(self.request, 'Veículo atualizado com sucesso.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Erro ao atualizar veículo.')
        return super().form_invalid(form)


class VeiculoDeleteView(LoginRequiredMixin, DeleteView):
    model = Veiculo
    success_url = reverse_lazy('veiculos:listar')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Veículo excluído com sucesso.")
        return super().delete(request, *args, **kwargs)
