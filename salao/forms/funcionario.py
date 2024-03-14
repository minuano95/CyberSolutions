from django import forms
from ..models import Funcionario

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['nome', 'cpf', 'telefone', 'email', 'endereco',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs.update({'class': 'funcionario-form'})
        self.fields['cpf'].widget.attrs.update({'class': 'funcionario-form'})
        self.fields['telefone'].widget.attrs.update({'class': 'funcionario-form', 'type': 'text'})
        self.fields['email'].widget.attrs.update({'class': 'funcionario-form'})
        self.fields['endereco'].widget.attrs.update({'class': 'funcionario-form'})


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
        print('telefone', telefone)
        # if '+' not in telefone:
        #     telefone = '+55' + telefone
        #     print(telefone)

        endereco = cleaned_data.get('endereco')
        if len(endereco) == 0:
            raise forms.ValidationError('Este campo não pode ficar em branco.')
        elif len(endereco) > 100:
            raise forms.ValidationError('O endereço não pode ter mais de 100 caracteres.')

        return cleaned_data
