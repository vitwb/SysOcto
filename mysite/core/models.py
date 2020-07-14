from django.db import models

class Corretor (models.Model):
    nome = models.CharField(max_length=100, help_text='Nome do Corretor')
    telefone = models.IntegerField()
    email = models.EmailField()
    cnpj = models.IntegerField()
    end =  models.CharField(max_length=500)

def __str__(self):
    return self.description

