from django.contrib.auth.models import User, Group
from rest_framework import serializers
from calcular.models import Calculadora


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class CalculadoraSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Calculadora
        fields = ['url', 'id', 'number_1', 'number_2', 'operacao', 'resultado']

    