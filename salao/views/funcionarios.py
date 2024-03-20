from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from ..models import Agendamento, Funcionario, Financeiro
from ..forms import AgendamentoForm, FuncionarioForm

@login_required(login_url='/salao/login/')
def funcionarios_view(request):
    """
    This Python function retrieves active employees from the database and renders them in a template for
    display.
    
    :param request: The `request` parameter in the `funcionarios_view` function is an HttpRequest object
    that Django passes to the view function when it's called. It contains information about the current
    web request, including metadata about the request, any data sent with the request, and other useful
    attributes and methods for processing
    :return: The `funcionarios_view` function is returning a rendered HTML template named
    'funcionarios.html' with a context containing the queryset of active `Funcionario` objects
    (employees) filtered by `status=True`. The template will be rendered with the list of active
    employees passed in the context.
    """
    funcionarios = Funcionario.objects.filter(status=True)   
    return render(request, 'salao/funcionarios/funcionarios.html', context={'funcionarios': funcionarios})

@login_required(login_url='/salao/login/')
def edita_funcionario(request, funcionario_id):
    """
    This Python function is used to edit a specific employee's information in a salon management system,
    requiring login authentication and utilizing a form for data input and validation.
    
    :param request: The `request` parameter in the `edita_funcionario` function is an HttpRequest object
    that represents the current HTTP request. It contains information about the request made by the
    client, such as the request method (GET, POST, etc.), user session data, and any data sent in the
    request (
    :param funcionario_id: The `funcionario_id` parameter in the `edita_funcionario` function represents
    the unique identifier of the employee (funcionário) that is being edited. This identifier is used to
    retrieve the specific employee object from the database using `get_object_or_404` function. It is
    typically an
    :return: The code snippet is a view function in Django that allows editing a specific employee
    (funcionario) in a salon management system. When a user accesses this view, they must be logged in,
    as indicated by the `@login_required` decorator.
    """   
    funcionario = get_object_or_404(Funcionario, pk=funcionario_id)
    agendamentos = Agendamento.objects.filter(funcionario=funcionario_id)    
    agendamentos_count = agendamentos.count()

    if request.method == 'POST':
        form = FuncionarioForm(request.POST, instance=funcionario)
        if form.is_valid():
            form.save()
            return redirect('salao:funcionarios')
    else:
        form = FuncionarioForm(instance=funcionario)  # Preencha o formulário 

    context = {
        'funcionario': funcionario, 
        'form': form, 
        'agendamentos': agendamentos,
        'agendamentos_count': agendamentos_count,
    }
    return render(request, 'salao/funcionarios/editar_funcionario.html', context=context)            
    
@login_required(login_url='/salao/login/')
def adiciona_funcionario(request):
    """
    The function `adiciona_funcionario` in Python handles the addition of a new employee to a form and
    saves the data if the form is valid.
    
    :param request: The `request` parameter in the `adiciona_funcionario` function is typically an
    HttpRequest object that represents the current HTTP request. It contains information about the
    request made by the client, such as the request method (GET, POST, etc.), request data, user session
    information, and more
    :return: The function `adiciona_funcionario` is returning a redirect to the 'salao:funcionarios' URL
    if the form is valid and successfully saved. If the form is not valid, it will print out the form
    errors.
    """
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
    """
    The function `exclui_funcionario` marks a specific employee as inactive and redirects to the list of
    employees.
    
    :param request: The `request` parameter in the `exclui_funcionario` function is an object that
    contains information about the current HTTP request. It includes details such as the user making the
    request, any data being sent with the request, and other metadata related to the request. In this
    context, the `
    :param funcionario_id: The `funcionario_id` parameter in the `exclui_funcionario` function
    represents the unique identifier of the employee (funcionário) that is being deleted or marked as
    inactive in this case. This parameter is used to retrieve the specific employee object from the
    database using the `get_object_or
    :return: The `exclui_funcionario` view function is returning a redirect response to the
    'salao:funcionarios' URL after setting the status of the specified employee (retrieved using the
    `funcionario_id`) to False and saving the changes.
    """
    funcionario = get_object_or_404(Funcionario, pk=funcionario_id)
    funcionario.status = False
    funcionario.save()
    
    return redirect('salao:funcionarios')


@login_required(login_url='/salao/login/')
def deleta_agendamento_funcionario(request, agendamento_id):
    agendamento = get_object_or_404(Agendamento, pk=agendamento_id)
    funcionario_id = agendamento.funcionario.id  # Obtém o ID do funcionário associado ao agendamento
    agendamento.delete()

    financeiro = get_object_or_404(Financeiro, agendamento_id=agendamento_id)
    if financeiro is not None:
        financeiro.delete()
    # Constrói a URL para a página de edição do funcionário
    url = reverse('salao:edita_funcionario', args=[funcionario_id])
    return redirect(url)
    