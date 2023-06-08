from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    pessoa = models.OneToOneField(Pessoa, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.pessoa.nome


class Veiculo(models.Model):
    placa = models.CharField(max_length=10, unique=True)
    descricao = models.CharField(max_length=255)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Veiculo'
        verbose_name_plural = 'Veiculos'

    def __str__(self):
        return self.descricao


class Mecanico(models.Model):
    pessoa = models.OneToOneField(Pessoa, on_delete=models.CASCADE)
    especialidade = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Mecânico'
        verbose_name_plural = 'Mecânicos'

    def __str__(self):
        return self.pessoa.nome


class Equipe(models.Model):
    descricao = models.CharField(max_length=255)
    mecanicos = models.ManyToManyField(Mecanico)

    class Meta:
        verbose_name = 'Equipe'
        verbose_name_plural = 'Equipes'

    def __str__(self):
        return self.descricao


class Peca(models.Model):
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Peça'
        verbose_name_plural = 'Peças'

    def __str__(self):
        return self.descricao


class Servico(models.Model):
    descricao = models.CharField(max_length=255)
    peca = models.ForeignKey(Peca, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'


class OS(models.Model):
    data_emissao = models.DateTimeField(auto_now_add=True)
    data_entrega = models.DateTimeField(null=True, blank=True)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Ordem de Serviço'
        verbose_name_plural = 'Ordens de Serviço'

    def __str__(self):
        return self.veiculo.descricao


class Item(models.Model):
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    os = models.ForeignKey(OS, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'

    def __str__(self):
        return self.descricao
