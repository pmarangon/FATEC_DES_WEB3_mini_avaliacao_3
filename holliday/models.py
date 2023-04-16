from django.db import models

class Holliday(models.Model):
  id = models.AutoField(primary_key=True)
 nome = models.CharField('Feriado',max_length=50)
 dia = models.IntegerField('Data')
 mes = models.IntegerField('Mês')
 def __str__(self):
 return self.nome
