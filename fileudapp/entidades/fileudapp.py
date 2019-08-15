class FileUDApp:

    def __init__(self, nome_arquivo, tipo_arquivo, arquivo):
        self.__nome_arquivo = nome_arquivo
        self.__tipo_arquivo = tipo_arquivo
        self.__arquivo = arquivo

    @property
    def nome_arquivo(self):
        return self.__nome_arquivo

    @nome_arquivo.setter
    def nome_arquivo(self, novo_nome):
        self.__nome_arquivo = novo_nome

    @property
    def tipo_arquivo(self):
        return self.__tipo_arquivo

    @tipo_arquivo.setter
    def tipo_arquivo(self, tipo):
        self.__tipo_arquivo = tipo

    @property
    def arquivo(self):
        return self.__arquivo

    @arquivo.setter
    def arquivo(self, novo_arquivo):
        self.__arquivo = novo_arquivo
