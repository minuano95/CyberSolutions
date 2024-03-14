from django import forms
from ..models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'cpf', 'telefone', 'email', 'divida', 'endereco',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs.update({'class': 'cliente-form'})
        self.fields['cpf'].widget.attrs.update({'class': 'cliente-form'})
        self.fields['telefone'].widget.attrs.update({'class': 'cliente-form', 'type': 'text'})
        self.fields['email'].widget.attrs.update({'class': 'cliente-form'})
        self.fields['divida'].widget.attrs.update({'class': 'cliente-form'})
        self.fields['endereco'].widget.attrs.update({'class': 'cliente-form'})


    def clean(self):
        cleaned_data = super().clean()

        nome = cleaned_data.get('nome')
        if len(nome) == 0:
            raise forms.ValidationError('Este campo não pode ficar em branco.')
        elif len(nome) > 100:
            raise forms.ValidationError('O nome não pode ter mais de 100 caracteres.')

        cpf = cleaned_data.get('cpf')
        print('cfp', cpf)
        if len(cpf) == 0:
            raise forms.ValidationError('Este campo não pode ficar em branco.')
        elif len(cpf) > 20:
            raise forms.ValidationError('O cpf não pode ter mais de 20 caracteres.')

        telefone = cleaned_data.get('telefone')
     
        endereco = cleaned_data.get('endereco')
        if len(endereco) == 0:
            raise forms.ValidationError('Este campo não pode ficar em branco.')
        elif len(endereco) > 100:
            raise forms.ValidationError('O endereço não pode ter mais de 100 caracteres.')

        return cleaned_data
