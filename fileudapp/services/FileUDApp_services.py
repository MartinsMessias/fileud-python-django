from ..models import FileUDApp


def listar_arquivos():
    arquivos = FileUDApp.objects.all()
    return arquivos


def listar_arquivo_id(id):
    arquivo = FileUDApp.objects.get(id=id)
    return arquivo


def remover_arquivo(arquivo):
    arquivo.delete()


def upload_arquivo(novo):
    FileUDApp.objects.create(
        nome_arquivo=novo.nome_arquivo,
        tipo_arquivo=novo.tipo_arquivo,
        arquivo=novo.arquivo
    )


def alterar_arquivo(arquivo, novo):
    arquivo.nome_arquivo = novo.nome_arquivo
    arquivo.tipo_arquivo = novo.tipo_arquivo
    arquivo.arquivo = novo.arquivo
    arquivo.save(force_update=True)
