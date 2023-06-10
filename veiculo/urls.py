from django.urls import path

from . import views
from .views import VeiculoDeleteView

app_name = 'veiculos'

urlpatterns = [
    path('', views.VeiculoListView.as_view(), name='listar'),
    path('novo/', views.VeiculoCreateView.as_view(), name='criar'),
    path('editar/<int:pk>/', views.VeiculoUpdateView.as_view(), name='atualizar'),
    path('<int:pk>/excluir/', VeiculoDeleteView.as_view(), name='excluir'),

]
