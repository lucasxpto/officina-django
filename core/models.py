from django.core.exceptions import ValidationError
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
    veiculos = models.ManyToManyField('Veiculo', through='VeiculoEquipe')

    class Meta:
        verbose_name = 'Equipe'
        verbose_name_plural = 'Equipes'

    def __str__(self):
        return self.descricao


class Veiculo(models.Model):
    placa = models.CharField(max_length=7)
    descricao = models.CharField(max_length=255)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='veiculos')
    equipes = models.ManyToManyField(Equipe, through='VeiculoEquipe')

    class Meta:
        verbose_name = 'Veículo'
        verbose_name_plural = 'Veículos'

    def __str__(self):
        return f'{self.placa} - {self.descricao} - {self.cliente}'


class VeiculoEquipe(models.Model):
    veiculo = models.ForeignKey('Veiculo', on_delete=models.CASCADE)
    equipe = models.ForeignKey('Equipe', on_delete=models.CASCADE)


class Servico(models.Model):
    descricao = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return f'{self.descricao} - R$ {self.preco}'


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
    equipe = models.ForeignKey('Equipe', on_delete=models.CASCADE)
    servicos = models.ManyToManyField(Servico)
    pecas = models.ManyToManyField(Peca, through='PecaOrdemServico')
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    class Meta:
        verbose_name = 'Ordem de Serviço'
        verbose_name_plural = 'Ordens de Serviço'

    def __str__(self):
        return self.veiculo.descricao

    def save(self, *args, **kwargs):
        self.total = 0
        for servico in self.servicos.all():
            self.total += servico.preco
        for peca_os in self.pecaordemservico_set.all():
            self.total += peca_os.peca.preco * peca_os.quantidade
        super().save(*args, **kwargs)


class PecaOrdemServico(models.Model):
    peca = models.ForeignKey(Peca, on_delete=models.CASCADE)
    ordem_servico = models.ForeignKey(OrdemServico, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Peça da Ordem de Serviço'
        verbose_name_plural = 'Peças da Ordem de Serviço'

    def __str__(self):
        return self.peca.descricao


class QuemSomos(models.Model):
    titulo = models.CharField(max_length=200)
    corpo = models.TextField()
    data_cadastro = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Quem Somos'
        verbose_name_plural = 'Quem Somos'

    def __str__(self):
        return self.titulo
