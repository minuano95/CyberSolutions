from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.db.models import Sum
from calendar import monthrange
from datetime import datetime
from ..models import Financeiro

@login_required(login_url='/salao/login/')
def financeiro_view(request):
    # Obter o primeiro registro financeiro
    primeiro_financeiro = Financeiro.objects.order_by('data').first()
    if primeiro_financeiro is None:
        # Se não houver registros financeiros, retorne uma resposta vazia ou faça o tratamento necessário
        return render(request, 'salao/financeiro/financeiro.html')

    # Obter o ano e o mês do primeiro registro
    primeiro_ano = primeiro_financeiro.data.year
    primeiro_mes = primeiro_financeiro.data.month

    # Obter o ano e o mês atual
    ano_atual = timezone.now().year
    mes_atual = timezone.now().month

    # Inicializar um dicionário para armazenar os dados mês a mês
    dados_por_mes = {}

    # Loop pelos anos
    for ano in range(primeiro_ano, ano_atual + 1):
        # Determinar o mês inicial e final do loop baseado no ano
        mes_inicial = primeiro_mes if ano == primeiro_ano else 1
        mes_final = mes_atual + 1 if ano == ano_atual else 13

        # Loop pelos meses
        for mes in range(mes_inicial, mes_final):
            # Calcular o primeiro e o último dia do mês
            primeiro_dia = timezone.make_aware(datetime(ano, mes, 1))
            ultimo_dia = timezone.make_aware(datetime(ano, mes, monthrange(ano, mes)[1], 23, 59, 59))

            # Filtrar os registros financeiros para o mês atual
            registros_do_mes = Financeiro.objects.filter(
                data__gte=primeiro_dia,
                data__lte=ultimo_dia,
            )

            # Calcular entradas e saídas
            entradas = registros_do_mes.filter(entrada__gt=0).aggregate(total=Sum('entrada'))['total'] or 0
            saidas = registros_do_mes.filter(saida__gt=0).aggregate(total=Sum('saida'))['total'] or 0

            # Calcular o saldo
            saldo = entradas - saidas

            # Armazenar os dados no dicionário
            if ano not in dados_por_mes:
                dados_por_mes[ano] = {}
            dados_por_mes[ano][mes] = {
                'entradas': f'R$ {round(entradas, 2)}',
                'saidas': f'R$ {round(saidas, 2)}',
                'saldo': f'R$ {round(saldo, 2)}',
            }

    print(dados_por_mes)
    
    return render(request, 'salao/financeiro/financeiro.html', {'dados_por_mes': dados_por_mes})
