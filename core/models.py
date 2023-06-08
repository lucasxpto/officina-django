from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255)


class Cliente(models.Model):
    pessoa = models.OneToOneField(Pessoa, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=255)


class Veiculo(models.Model):
    placa = models.CharField(max_length=10, unique=True)
    descricao = models.CharField(max_length=255)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)


class Mecanico(models.Model):
    pessoa = models.OneToOneField(Pessoa, on_delete=models.CASCADE)
    especialidade = models.CharField(max_length=100)


class Equipe(models.Model):
    descricao = models.CharField(max_length=255)
    mecanicos = models.ManyToManyField(Mecanico)


class Peca(models.Model):
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)


class Servico(models.Model):
    descricao = models.CharField(max_length=255)
    peca = models.ForeignKey(Peca, on_delete=models.CASCADE)


class OS(models.Model):
    data_emissao = models.DateField()
    data_entrega = models.DateField(null=True, blank=True)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE)


class Item(models.Model):
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    os = models.ForeignKey(OS, on_delete=models.CASCADE)
