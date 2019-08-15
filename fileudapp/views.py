from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from .entidades import fileudapp
from .services import FileUDApp_services


def upload(request):
    if request.method == 'POST':
        form = FileUDAppForm(request.POST, request.FILES)

        if form.is_valid():
            nome_arquivo = form.cleaned_data['nome_arquivo']
            tipo_arquivo = form.cleaned_data['tipo_arquivo']
            arquivo = form.cleaned_data['arquivo']

            novo = fileudapp.FileUDApp(nome_arquivo=nome_arquivo, tipo_arquivo=tipo_arquivo, arquivo=arquivo)

            FileUDApp_services.upload_arquivo(novo)

            messages.info(request, 'Arquivo upado!')
            return redirect(arquivos)
        else:
            messages.warning(request, 'Houve um erro!')
            return render(request, 'fileudapp/upload.html', {'form': form})

    else:
        form = FileUDAppForm()
        return render(request, 'fileudapp/upload.html', {'form': form})


def arquivos(request):
    arquivos = FileUDApp_services.listar_arquivos()

    if not arquivos:
        messages.info(request, 'Sem arquivos para exibir!')
        return render(request, 'fileudapp/arquivos.html')

    return render(request, 'fileudapp/arquivos.html', {'arquivos': arquivos})


def remover(request, id):
    obj = get_object_or_404(FileUDApp, pk=id)
    FileUDApp_services.remover_arquivo(obj)

    messages.info(request, 'Arquivo removido com sucesso!')

    return redirect(arquivos)


def alterar(request, id):
    arquivo_a = FileUDApp_services.listar_arquivo_id(id)
    form = FileUDAppForm(request.POST or None, instance=arquivo_a)

    if form.is_valid():
        nome_arquivo = form.cleaned_data['nome_arquivo']
        tipo_arquivo = form.cleaned_data['tipo_arquivo']
        arquivo = form.cleaned_data['arquivo']

        novo = fileudapp.FileUDApp(nome_arquivo=nome_arquivo, tipo_arquivo=tipo_arquivo, arquivo=arquivo)

        FileUDApp_services.alterar_arquivo(arquivo_a, novo)

        messages.info(request, 'Arquivo alterado com sucesso!')

        return redirect(arquivos)

    return render(request, 'fileudapp/exibir.html', {'form': form})
