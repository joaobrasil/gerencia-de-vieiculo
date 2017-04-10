from django.shortcuts import render

# Create your views here.
from veiculo.models import Tipo_veiculo

def index(request):
    consulta_no_banco=Tipo_veiculo.objects.all()

    return render(request,'index.html',
                   {'consulta_no_banco':consulta_no_banco})
