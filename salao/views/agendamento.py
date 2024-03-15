
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from ..models import Agendamento, Financeiro
from ..forms import AgendamentoForm
from datetime import datetime

# Django-apscheduler
# from apscheduler.schedulers.background import BackgroundScheduler
# from apscheduler.triggers.interval import IntervalTrigger

# twilio
# from twilio.rest import Client


@login_required(login_url='/salao/login/')
def index(request):
    return render(request, 'salao/home.html')


@login_required(login_url='/salao/login/')
def agenda_view(request):
    if request.method == 'POST' and 'selected_date' in request.POST:
        selected_date = request.POST.get('selected_date')
        agendamentos = Agendamento.objects.filter(status=False, data_inicio__date=selected_date).order_by('data_inicio')
        print(len(agendamentos))  # Para verificar o número de agendamentos filtrados

        return render(request, 'salao/agenda/agenda.html', {'agendamentos': agendamentos})
    else:
        agendamentos = Agendamento.objects.filter(status=False).order_by('data_inicio')
        print(len(agendamentos))  # Para verificar o número de todos os agendamentos

        return render(request, 'salao/agenda/agenda.html', {'agendamentos': agendamentos})

@login_required(login_url='/salao/login/')
def novo_agendamento(request):
    form = AgendamentoForm()
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            data_inicio = form.cleaned_data['data_inicio']
            data_final = form.cleaned_data['data_final']
            funcionario = form.cleaned_data['funcionario']

            # Verifique se o funcionário já possui um agendamento no intervalo de tempo especificado
            agendamentos = Agendamento.objects.filter(
                funcionario=funcionario,
                data_inicio__lte=data_final,
                data_final__gte=data_inicio
            )

            if agendamentos.first() is not None:
                # Caso exista um agendamento para o funcionário no intervalo de tempo
                form.add_error(None, "Este funcionário já possui um agendamento no mesmo intervalo de tempo.")
            else:
                form.save()
                return redirect('salao:agenda')
    else:
        form = AgendamentoForm()

    return render(request, 'salao/agenda/novo_agendamento.html', {'form': form})


@login_required(login_url='/salao/login/')
def edita_agendamento(request, agendamento_id):
    # agendamento = Agendamento.objects.get(pk=agendamento_id)
    # data = {
    #     'titulo': agendamento.titulo,
    #     'descricao': agendamento.descricao,
    #     'cliente': agendamento.cliente,
    #     'funcionario': agendamento.funcionario,
    #     'preco': agendamento.preco,
    #     'data_inicio': agendamento.data_inicio,
    #     'data_final': agendamento.data_final,
    # }

    agendamento = get_object_or_404(Agendamento, pk=agendamento_id)

    if request.method == 'POST':
        form = AgendamentoForm(request.POST, instance=agendamento)
        if form.is_valid():
            form.save()
            return redirect('salao:agenda')
    else:
        form = AgendamentoForm(instance=agendamento)  # Preencha o formulário 
    return render(request, 'salao/agenda/editar_agendamento.html', {'agendamento': agendamento, 'form': form})


@login_required(login_url='/salao/login/')
def deleta_agendamento(request, agendamento_id):
    agendamento = get_object_or_404(Agendamento, pk=agendamento_id)
    agendamento.status = True
    agendamento.save()
    return redirect('salao:agenda')


@login_required(login_url='/salao/login/')
def atualiza_agendamento(request, agendamento_id):
    if request.method == 'POST':
        agendamento = Agendamento.objects.get(pk=agendamento_id)
        agendamento.concluido = True
        agendamento.save()
        
        novo_registro_financeiro = Financeiro(
            entrada = agendamento.preco,
            saida = 0,
            descricao = f'{agendamento.id} | {agendamento.titulo} | {agendamento.cliente} | {agendamento.funcionario}',
            is_agendamento = True,
            id_agendamento = agendamento_id,
            data = datetime.now()       
        )
        
        novo_registro_financeiro.save()
        print('Registro salvo')
        
        return redirect('salao:agendamentos_concluidos')
    return redirect('salao:agenda')


@login_required(login_url='/salao/login/')
def agendamentos_concluidos(request):
    return redirect('salao:home')

# Mensagens
# def enviaLembrete():
#     # Dados da conta do Twilio
#     account_sid = 'ACc3d46529b185e0e2ca09ab74738f0a50'
#     auth_token = 'd2b7876a4750b35470821f65b0616697'
#     client = Client(account_sid, auth_token)

#     # Número do WhatsApp remetente
#     from_whatsapp_number = 'whatsapp:+5517997023612'

#     # Mensagem e número do cliente
#     message = client.messages.create(
#         body='Lembrete: Seu horário no salão de beleza é amanhã às 10h.',
#         from_=from_whatsapp_number,
#         to='whatsapp:+5517997023612'
#     )

#     print(message.sid)
#     # print('Teste')

# # Adicionando o agendador a função
# scheduler = BackgroundScheduler()
# scheduler.add_job(enviaLembrete, trigger=IntervalTrigger(minutes=1))
# scheduler.start()
