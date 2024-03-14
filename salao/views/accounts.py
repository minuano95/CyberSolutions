from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import redirect 
from ..forms import CustomAuthenticationForm

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        print(form.is_valid())
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = form.get_user()
            if user is not None:
                login(request, user)
                return redirect('salao:home')  # Redirecionamento para a página inicial usando o nome definido na URL
        
        if not form.is_valid():
            messages.error(request, 'Usuário ou senha incorreta.')
    
    else:
        form = CustomAuthenticationForm()
        
    return render(request, 'salao/accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('salao:accounts')