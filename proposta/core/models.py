# from __future__ import unicode_literals
from django.db import models
from localflavor.br.br_states import STATE_CHOICES

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(u'Nome', max_length=100)
    def __str__(self):
        return self.nome

class Proposta(models.Model):
    cliente = models.ForeignKey("Cliente", on_delete=models.CASCADE)
    cpf = models.CharField(u'CPF', blank=True, max_length=14)
    cnpj = models.CharField(u'CNPJ', blank=True, max_length=18)
    endereco = models.CharField(u'Endereço', blank=True, max_length=200)
    bairro = models.CharField(u'Bairro', blank=True, max_length=100)
    cidade = models.CharField(u'Cidade', blank=True, max_length=100)
    estado = models.CharField(max_length=2, null=True, blank=True, choices=STATE_CHOICES)
    data = models.DateTimeField(u'Data de Emissão')
    VALIDADE_CHOICES = (
        ('Quinta', '15 (Quinze)'),
        ('Trinta', '30 (Trinta)'),
        ('Sessenta', '60 (Sessenta)'),
    )
    validade = models.CharField(u'Validade', blank=True, max_length=200, choices=VALIDADE_CHOICES)
    valor = models.DecimalField(u'Valor a pagar', max_digits=8, decimal_places=2)
    CATEGORY_CHOICES = (
        ('Atrasado', 'Atrasado'),
        ('AVencer', 'Á Vencer'),
        ('Pago', 'Pago')
    )
    situacao = models.CharField(u'Situação', max_length=200, choices=CATEGORY_CHOICES)
    pago = models.BooleanField(default=False)
    dominio = models.CharField(u'Domínio do Site', blank=True, max_length=200, help_text='URL - exe: seudomonio.com.br')
    dominio_login = models.CharField(u'Acesso ao Admin', blank=True, max_length=200, help_text='URL - exe: seu dominio/admin')
    senha = models.CharField(u'Senha', max_length=30, blank=True)

    class Meta:
        ordering = ['-data']
        verbose_name = u'UMA PROPOSTA'
        verbose_name_plural = u'PROPOSTAS'

    def __str__(self):
        if self.cliente.nome:
            return self.cliente.nome
        else:
            return self.custom_alias_name