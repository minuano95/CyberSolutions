from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from ..models import Cliente, Agendamento, Funcionario, Cliente
from ..forms import AgendamentoForm, FuncionarioForm, ClienteForm


@login_required(login_url='/salao/login/')
def clientes_view(request):
    clientes = Cliente.objects.filter(status=True)   
    return render(request, 'salao/clientes/clientes.html', context={'clientes': clientes})

@login_required(login_url='/salao/login/')
def edita_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    # agendamentos = Agendamento.objects.filter(cliente=cliente_id)    

    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        print(type(form))
        if form.is_valid():
            form.save()
            return redirect('salao:clientes')
    else:
        form = ClienteForm(instance=cliente)  # Preencha o formulário 
        
    return render(request, 'salao/clientes/editar_cliente.html', {'cliente': cliente, 'form': form})            
    
@login_required(login_url='/salao/login/')
def adiciona_cliente(request):
    form = ClienteForm()
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('salao:clientes')
    else:
        form = ClienteForm()
    
    return render(request, 'salao/clientes/adiciona_cliente.html', context={'form': form})

@login_required(login_url='/salao/login/')
def exclui_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    cliente.status = False
    cliente.save()
    
    return redirect('salao:clientes')