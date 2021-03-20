from django.contrib import admin
from calcular.models import Calculadora


@admin.register(Calculadora)
class CalculadoraAdmin(admin.ModelAdmin):
    fields = ('number_1', 'number_2', 'operacao', )
    list_display = ('number_1', 'number_2', 'operacao', 'resultado')
    search_fields = ['operacao']


    def resultado(self, obj):
        if obj.operacao == 'soma':
            return obj.number_1 + obj.number_2
        elif obj.operacao == 'subtracao':
            return obj.number_1 - obj.number_2
        elif obj.operacao == 'multiplicacao':
            return obj.number_1 * obj.number_2
        elif obj.operacao == 'divisao':
           return obj.number_1 / obj.number_2
