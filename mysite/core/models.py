from django.db import models

class Corretor (models.Model):
    nome = models.CharField(max_length=200, help_text='Nome do Corretor')
    telefone = models.IntegerField()
    email = models.EmailField()
    cnpj = models.IntegerField()
    end =  models.CharField(max_length=500)
    def __str__(self):
        return self.nome

class Produto (models.Model):
    empreendimento = models.CharField(max_length=100, help_text='Nome do empreendimento')
    cidade = models.CharField(max_length=100, help_text='Cidade')
    estado = models.CharField(max_length=100, help_text='Estado')
    bairro = models.CharField(max_length=100, help_text='Bairro')
    rua =  models.CharField(max_length=500)
    numero = models.IntegerField(null = True)
    tipologia = models.CharField(max_length=500, help_text='Tipologia')
    link = models.CharField(max_length=200)
    def __str__(self):
        return self.empreendimento
        
class Cliente (models.Model):
    Corretores = models.ForeignKey(Corretor, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200, help_text='Nome do cliente')
    telefone = models.IntegerField()
    email = models.EmailField()
    cpf = models.IntegerField(null= True)
    end =  models.CharField(max_length=500)
    date_created = models.DateTimeField(auto_now_add=True , null = True)
    def __str__(self):
        return self.nome

class Atendimento (models.Model):
    corretores = models.ForeignKey(Corretor, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True , null = True)

