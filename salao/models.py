from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=20)
    telefone = PhoneNumberField(default='+55', region='BR')
    email = models.EmailField()
    divida = models.FloatField()
    endereco = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    
    
    def __str__(self):
        return f'{self.id} | {self.nome}'
    
class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=20)
    telefone = PhoneNumberField(default='+55', region='BR')
    email = models.EmailField()
    endereco = models.CharField(max_length=100)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.id} | {self.nome}'
    
class Agendamento(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=150)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, limit_choices_to={'status': True})
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE, limit_choices_to={'status': True})
    preco = models.FloatField()
    data_inicio = models.DateTimeField()
    data_final = models.DateTimeField()
    concluido = models.BooleanField(default=False)
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.titulo} em {self.data_inicio}'
    
    
class Financeiro(models.Model):
    entrada = models.FloatField()
    saida = models.FloatField()
    descricao = models.CharField(max_length=100)
    is_agendamento = models.BooleanField(default=False)
    id_agendamento = models.CharField(max_length=3, blank=True)
    data = models.DateTimeField()
    
    def __str__(self) -> str:
        if self.entrada > 0:
            return f'Entrada: {self.entrada}'
        
        return f'Saída: {self.saida}'