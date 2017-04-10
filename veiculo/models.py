from django.db import models

# Create your models here.
class Tipo_veiculo(models.Model):
    """
    Classe referente a tabela veiculo
    """
    tipo = models.CharField('Tip de Veiculo',max_length=20,help_text='Ex, Carro ou Moto')
    def __str__(self):
        return '{}'.format(self.tipo)
    class Meta:
        ordering=('tipo',)
        verbose_name ='Tipo de Veiculo'
        verbose_name_plural='Tipos de Veiculos'

class MarcadoVeiculo(models.Model):
    marca=models.CharField('Marca do Veiculos', max_length=20, help_text='Ex.Nissan, Honda,Fiat')
    def __str__(self):
        return '{}'.format(self.marca)

class Veiculo(models.Model):
    tipo=models.ForeignKey(Tipo_veiculo)
    marca=models.ForeignKey(MarcadoVeiculo)

    placa=models.CharField('Placa',max_length=10)
    cor=models.CharField('Cor',max_length=10)


    def __str__(self):
        return '{}-{}'.format(self.Placa,self.cor)

class Meta:
        ordering = ('tipo', 'marca', 'modelo')
        verbose_name = 'Veículo'
        verbose_name_plural = 'Veículos'
