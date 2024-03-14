from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from ..models import Cliente, Agendamento, Funcionario
from ..forms import AgendamentoForm, FuncionarioForm

@login_required(login_url='/salao/login/')
def funcionarios_view(request):
    funcionarios = Funcionario.objects.filter(status=True)   
    return render(request, 'salao/funcionarios/funcionarios.html', context={'funcionarios': funcionarios})

@login_required(login_url='/salao/login/')
def edita_funcionario(request, funcionario_id):
    funcionario = get_object_or_404(Funcionario, pk=funcionario_id)
    # agendamentos = Agendamento.objects.filter(funcionario=funcionario_id)    

    if request.method == 'POST':
        form = FuncionarioForm(request.POST, instance=funcionario)
        print(type(form))
        if form.is_valid():
            form.save()
            return redirect('salao:funcionarios')
    else:
        form = FuncionarioForm(instance=funcionario)  # Preencha o formulário 
        
    return render(request, 'salao/funcionarios/editar_funcionario.html', {'funcionario': funcionario, 'form': form})            
    
@login_required(login_url='/salao/login/')
def adiciona_funcionario(request):
    form = FuncionarioForm()
    print('METHOD:', request.method)
    if request.method == 'POST':
        form = FuncionarioForm(request.POST)
        print('FORM STATUS:', form.is_valid())
        if form.is_valid():
            print(form.cleaned_data)

            form.save()
            return redirect('salao:funcionarios')
        else:
            print(form.errors)
    else:
        form = FuncionarioForm()
    
    return render(request, 'salao/funcionarios/adiciona_funcionario.html', context={'form': form})

@login_required(login_url='/salao/login/')
def exclui_funcionario(request, funcionario_id):
    funcionario = get_object_or_404(Funcionario, pk=funcionario_id)
    funcionario.status = False
    funcionario.save()
    
    return redirect('salao:funcionarios')