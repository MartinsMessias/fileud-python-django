from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from  .forms import *
from .models import *

def upload(request):

    if request.method == 'POST':
        form = FileUDAppForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.info(request, 'Arquivo upado!')
            return redirect(arquivos)
        else:
            messages.warning(request, 'Houve um erro!')
            return render(request, 'fileudapp/upload.html', {'form': form})

    else:
        form = FileUDAppForm()
        return render(request, 'fileudapp/upload.html', {'form':form})


def arquivos(request):
    arquivos = FileUDApp.objects.all().order_by('-data_upload')

    if not arquivos:
        messages.info(request, 'Sem arquivos para exibir!')
        return render(request, 'fileudapp/arquivos.html')

    return render(request, 'fileudapp/arquivos.html', {'arquivos': arquivos})


def remover(request, id):
    obj = get_object_or_404(FileUDApp, pk=id)
    obj.delete()
    messages.info(request, 'Arquivo removido com sucesso!')
    return redirect(arquivos)


def alterar(request, id):
    obj = get_object_or_404(FileUDApp, pk=id)
    return render(request, 'fileudapp/exibir.html', {'infos':obj})