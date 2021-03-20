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

    def resultado(self):
        if self.operacao == 'soma':
            return self.number_1 + self.number_2
        elif self.operacao == 'subtracao':
            return self.number_1 - self.number_2
        elif self.operacao == 'multiplicacao':
            return self.number_1 * self.number_2
        elif self.operacao == 'divisao':
            return self.number_1 / self.number_2

    class Meta:
        verbose_name = "calculo"

    def __str__(self):
        return f'{self.operacao}'