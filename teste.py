import mysql.connector
from faker import Faker
from datetime import datetime, timedelta
import random


conn = mysql.connector.connect(
    host='18.228.46.31',
    user='minuano95',
    password='11223344',
    database='cybersolutions',  
    port='3306'     
)

cursor = conn.cursor()
cursor.execute('SELECT * FROM salao_financeiro')

for financeiro in cursor.fetchall():
    print(financeiro)
    # id = financeiro[0]
    # cursor.execute('DELETE FROM salao_financeiro WHERE id=%s', (id,))
    # conn.commit()


# cursor.execute('SELECT id, titulo, status FROM salao_agendamento')
# for agendamento in cursor.fetchall():
#     print(agendamento[0])
#     print(agendamento[1])
#     print(agendamento[2])
#     if agendamento[2] == 1:
#         cursor.execute('DELETE FROM salao_agendamento WHERE id=%s', (agendamento[0],))
#         conn.commit()

# def gerar_dados_funcionario():
#     fake = Faker('pt_BR')
#     nome = fake.name()
#     cpf = fake.cpf()
#     telefone = fake.phone_number()
#     email = fake.email()
#     divida = round(random.uniform(0, 10000), 2)
#     endereco = fake.address()
#     status = random.choice([True, False])
#     return (nome, cpf, telefone, email, divida, endereco, status)


def gerar_dados_agendamento_ultimos_6_meses():
    fake = Faker('pt_BR')
    
    # Gera um título aleatório, descrição e seleciona IDs aleatórios para cliente e funcionário
    titulo = fake.word()
    cliente_id = 1 # random.randint(1)
    funcionario_id = 1 #random.randint(1)
    descricao = fake.sentence()
    preco = round(random.uniform(50, 200), 2)
    
    # Calcula uma data de início aleatória nos últimos 6 meses
    dias_no_passado = random.randint(0, 180)  # Aproximadamente 6 meses
    data_inicio = datetime.now() - timedelta(days=dias_no_passado)
    
    # Define a duração do agendamento entre 1 a 4 horas e calcula a data final
    data_final = data_inicio + timedelta(hours=random.randint(1, 4))
    
    # Decide aleatoriamente se o agendamento foi concluído e o seu status
    concluido = random.choice([False])
    
    return (titulo, descricao, cliente_id, funcionario_id, preco, data_inicio, data_final, concluido,)


# # Cria 10 agendamentos
# for _ in range(10):
#     dados = gerar_dados_agendamento_ultimos_6_meses()
#     # Query SQL para inserir os dados do agendamento
#     query = "INSERT INTO salao_agendamento (titulo, descricao, cliente_id, funcionario_id, preco, data_inicio, data_final, concluido) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
#     cursor.execute(query, dados)
#     conn.commit()
    
# cursor.execute("DELETE FROM salao_cliente")
# cursor.execute("DELETE FROM salao_agendamento")
# cursor.execute("DELETE FROM salao_funcionario")

# Commit para salvar as alterações