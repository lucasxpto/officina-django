from django.urls import path

from . import views

app_name = 'veiculos'

urlpatterns = [
    path('', views.VeiculoListView.as_view(), name='list'),
]
