from django.db import models

# Create your models here.

def user_directory_path(instance, filename):
    return 'docs/{0}/{1}'.format(instance.tipo_arquivo, filename)

class FileUDApp(models.Model):

    TIPO_ARQUIVO = (
        ('imagem', 'Imagem'),
        ('audio', 'Audio'),
        ('outro', 'Outro'))

    nome_arquivo = models.CharField(max_length=250, blank=False, null=False)
    tipo_arquivo = models.CharField(max_length=6, choices=TIPO_ARQUIVO, blank=False, null=False)
    arquivo = models.FileField(upload_to=user_directory_path, default='docs/arquivos_uploaded/nofile')
    data_upload = models.DateField(auto_now_add=True)
    data_modficacao = models.DateField(auto_now=True)

    def __str__(self):
        return self.nome_arquivo