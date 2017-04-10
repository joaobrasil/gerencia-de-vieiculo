# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-08 16:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MarcadoVeiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(help_text='Ex.Nissan, Honda,Fiat', max_length=20, verbose_name='Marca do Veiculos')),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_veiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(help_text='Ex, Carro ou Moto', max_length=20, verbose_name='Tip de Veiculo')),
            ],
            options={
                'ordering': ('tipo',),
                'verbose_name': 'Tipo de Veiculo',
                'verbose_name_plural': 'Tipos de Veiculos',
            },
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=8, verbose_name='Placa')),
                ('cor', models.CharField(max_length=10, verbose_name='Cor')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='veiculo.MarcadoVeiculo')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='veiculo.Tipo_veiculo')),
            ],
        ),
    ]