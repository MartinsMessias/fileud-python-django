from django import forms
from .models import FileUDApp


class FileFieldForm(forms.Form):
    arquivo = forms.FileField()


class FileUDAppForm(forms.ModelForm):
    class Meta:
        model = FileUDApp
        fields = ('nome_arquivo', 'tipo_arquivo', 'arquivo')

    def __init__(self, *args, **kwargs):
        for l in self.base_fields:
            self.base_fields[l].widget.attrs['class'] = 'form-control'

        super(FileUDAppForm, self).__init__(*args, **kwargs)
