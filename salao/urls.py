from django.urls import path
from .views import *

app_name = 'salao'

urlpatterns = [
    path('', index, name='home'),
    path('agenda/', agenda_view, name='agenda'),
    path('agenda/agendamentos_concluidos/', agendamentos_concluidos, name='agendamentos_concluidos'),
    path('agenda/novo_agendamento/', novo_agendamento, name='novo_agendamento'),
    path('agenda/edita_agendamento/<int:agendamento_id>/', edita_agendamento, name='edita_agendamento'),
    path('agenda/deleta_agendamento/<int:agendamento_id>/', deleta_agendamento, name='deleta_agendamento'),
    path('agenda/atualiza_agendamento/<int:agendamento_id>/', atualiza_agendamento, name='atualiza_agendamento'),
    
    path('funcionarios/', funcionarios_view, name='funcionarios'),
    path('funcionarios/edita_funcionario/<int:funcionario_id>/', edita_funcionario, name="edita_funcionario"),
    path('funcionarios/exclui_funcionario/<int:funcionario_id>/', exclui_funcionario, name="exclui_funcionario"),
    path('funcionarios/adiciona_funcionario/', adiciona_funcionario, name="adiciona_funcionario"),
    path('funcionarios/deleta_agendamento_funcionario/<int:agendamento_id>/', deleta_agendamento_funcionario, name="deleta_agendamento_funcionario"),

    path('clientes/', clientes_view, name='clientes'),
    path('clientes/edita_cliente/<int:cliente_id>/', edita_cliente, name="edita_cliente"),
    path('clientes/exclui_cliente/<int:cliente_id>/', exclui_cliente, name="exclui_cliente"),
    path('clientes/adiciona_cliente/', adiciona_cliente, name="adiciona_cliente"),

    path('financeiro/', financeiro_view, name='financeiro'),

    path('login/', login_view, name='accounts'),
    path('logout/', logout_view, name='signout')
]