import mysql.connector
from faker import Faker
from datetime import datetime, timedelta
import random


conn = mysql.connector.connect(
    host='18.231.73.132',
    user='minuano95',
    password='Ruizdesangue00.',
    database='cybersolutions'       
)

cursor = conn.cursor()

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


# def gerar_dados_agendamento():
#     fake = Faker('pt_BR')
#     titulo = fake.word()
#     cliente_id = random.randint(46,66)
#     funcionario_id = random.randint(87,91)
#     descricao = fake.sentence()
#     preco = round(random.uniform(50, 200), 2)
#     data_inicio = datetime.now() + timedelta(days=random.randint(-365, 365))
#     data_final = data_inicio + timedelta(hours=random.randint(1, 4))
#     concluido = random.choice([True, False])
#     status = random.choice([True, False])
#     return (titulo, descricao, cliente_id, funcionario_id, preco, data_inicio, data_final, concluido, status)

# # Cria 10 agendamentos
# for _ in range(10):
#     dados = gerar_dados_agendamento()
#     # Query SQL para inserir os dados do agendamento
#     query = "INSERT INTO salao_agendamento (titulo, descricao, cliente_id, funcionario_id, preco, data_inicio, data_final, concluido, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
#     cursor.execute(query, dados)
#     conn.commit()
    
# cursor.execute("DELETE FROM salao_cliente")
# cursor.execute("DELETE FROM salao_agendamento")
# cursor.execute("DELETE FROM salao_funcionario")

# Commit para salvar as alterações