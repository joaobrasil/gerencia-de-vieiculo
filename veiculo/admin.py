from django.contrib import admin

# Register your models here.

from veiculo.models import Tipo_veiculo, MarcadoVeiculo, Veiculo

admin.site.register(Tipo_veiculo)
admin.site.register(MarcadoVeiculo)
admin.site.register(Veiculo)
