from django.contrib.auth.models import User, Group
from rest_framework import serializers
from calcular.models import Calculadora
from calcular.models import Soma
from calcular.models import Subtracao 
from calcular.models import Multiplicacao
from calcular.models import Divisao




class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'password']

class SomaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Soma
        fields = ['url', 'id', 'number_1', 'number_2', 'resultado']


class SubtracaoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subtracao
        fields = ['url', 'id', 'number_1', 'number_2', 'resultado']


class MultiplicacaoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Multiplicacao
        fields = ['url', 'id', 'number_1', 'number_2', 'resultado']


class DivisaoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Divisao
        fields = ['url', 'id', 'number_1', 'number_2', 'resultado']

class CalculoSerializer():
    pass

    