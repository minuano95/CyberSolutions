from django import forms
from ..models import Agendamento


class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['titulo', 'descricao', 'cliente', 'funcionario', 'preco', 'data_inicio', 'data_final', 'concluido']

        widgets = {
            'descricao': forms.Textarea(attrs={'class': 'agendamento-form'}),
            'data_inicio': forms.DateTimeInput(format='%d/%m/%Y %H:%M', attrs={'class': 'agendamento-form', }),
            'data_final': forms.DateTimeInput(format='%d/%m/%Y %H:%M', attrs={'class': 'agendamento-form', }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['titulo'].widget.attrs.update({'class': 'agendamento-form'})
        self.fields['descricao'].widget.attrs.update({'class': 'agendamento-form'})
        self.fields['cliente'].widget.attrs.update({'class': 'agendamento-form'})
        self.fields['funcionario'].widget.attrs.update({'class': 'agendamento-form'})
        self.fields['preco'].widget.attrs.update({'class': 'agendamento-form'})
        self.fields['data_inicio'].widget.attrs.update({'class': 'agendamento-form'})
        self.fields['data_final'].widget.attrs.update({'class': 'agendamento-form'})
        self.fields['concluido'].widget.attrs.update({'class': 'agendamento-form'})

    def clean_preco(self):
        preco = self.cleaned_data['preco']
        # Faça sua validação do campo 'preco' aqui
        if preco < 0:
            raise forms.ValidationError("O preço não pode ser negativo.")
        return preco

    def clean(self):
        cleaned_data = super().clean()

        titulo = cleaned_data.get('titulo')
        if len(titulo) == 0:
            raise forms.ValidationError('Este campo não pode ficar em branco.')

        descricao = cleaned_data.get('descricao')
        if len(descricao) == 0:
            raise forms.ValidationError('Este campo não pode ficar em branco.')

        data_inicio = cleaned_data.get('data_inicio')
        data_final = cleaned_data.get('data_final')

        # Validação global entre os campos 'data_inicio' e 'data_final'
        if data_inicio and data_final and data_inicio >= data_final:
            raise forms.ValidationError("A data de início deve ser anterior à data final.")

        return cleaned_data
