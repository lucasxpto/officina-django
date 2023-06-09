from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=255)
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


class Mecanico(models.Model):
    pessoa = models.OneToOneField(Pessoa, on_delete=models.CASCADE)
    especialidade = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Mecânico'
        verbose_name_plural = 'Mecânicos'

    def __str__(self):
        return self.pessoa.nome


class Equipe(models.Model):
    descricao = models.CharField(max_length=255)
    mecanicos = models.ManyToManyField(Mecanico, related_name='equipes')

    class Meta:
        verbose_name = 'Equipe'
        verbose_name_plural = 'Equipes'

    def __str__(self):
        return self.descricao


class Veiculo(models.Model):
    placa = models.CharField(max_length=7)
    descricao = models.CharField(max_length=255)
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE, related_name='veiculo')

    class Meta:
        verbose_name = 'Veículo'
        verbose_name_plural = 'Veículos'

    def __str__(self):
        return self.descricao


class Servico(models.Model):
    descricao = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.descricao


class Peca(models.Model):
    descricao = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Peça'
        verbose_name_plural = 'Peças'

    def __str__(self):
        return self.descricao


class OrdemServico(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    servicos = models.ManyToManyField(Servico)
    pecas = models.ManyToManyField(Peca, through='PecaOrdemServico')
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    class Meta:
        verbose_name = 'Ordem de Serviço'
        verbose_name_plural = 'Ordens de Serviço'

    def __str__(self):
        return self.veiculo.descricao


class PecaOrdemServico(models.Model):
    peca = models.ForeignKey(Peca, on_delete=models.CASCADE)
    ordem_servico = models.ForeignKey(OrdemServico, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Peça da Ordem de Serviço'
        verbose_name_plural = 'Peças da Ordem de Serviço'

    def __str__(self):
        return self.peca.descricao
