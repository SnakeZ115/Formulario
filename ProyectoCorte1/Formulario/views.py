from django.shortcuts import render
from .forms import RegistrosForm
from .models import Carreras

# Create your views here.

def fomulario(request):
    form = RegistrosForm()
    carreras = Carreras.objects.all()
    return render(request, 'index.html', {'form': form, 'carreras': carreras})


def subir(request):
    carreras = Carreras.objects.all()
    if request.method == 'POST':
        form = RegistrosForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = RegistrosForm()
    
    return render(request, 'index.html', {'form': form, 'carreras': carreras})

