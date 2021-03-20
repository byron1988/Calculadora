from django.db import models

# Create your models here.
OPERACOES = (
        ('soma', 'Soma'),
        ('subtracao', 'Subtração'),
        ('multiplicacao', 'Multiplicação'),
        ('divisao', 'Divisão')
    )

class Calculadora(models.Model):
    """
    classe para o calculo
    """
    id = models.AutoField(primary_key=True)
    number_1 = models.IntegerField()
    number_2 = models.IntegerField()
    operacao = models.CharField(choices=OPERACOES, max_length=13)


    def somar(self):
        if self.operacao == 'soma':
            return self.number_1 + self.number_2

    def subtrair(self):
        if self.operacao == 'subtracao':
            return self.number_1 - self.number_2

    def multiplicar(self):
        if self.operacao == 'multiplicacao':
            return self.number_1 * self.number_2

    def dividir(self):
        if self.operacao == 'divisao':
            return self.number_1 / self.number_2
 


    class Meta:
        verbose_name = "calculo"

    def __str__(self):
        return f'{self.operacao}'