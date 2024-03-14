from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs.update({
            'class': 'fadeIn second',  # Classe do CSS para o campo de username
            'placeholder': 'Login',
            'id': 'username'
        })
        
        self.fields['password'].widget.attrs.update({
            'class': 'fadeIn third',  # Classe do CSS para o campo de password
            'placeholder': ' Senha',
            'id': 'password',
        })