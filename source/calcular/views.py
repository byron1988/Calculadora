from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from calcular.models import Calculadora
from calcular.serializers import UserSerializer, CalculadoraSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class CalculadoraViewSet(viewsets.ModelViewSet):

    queryset = Calculadora.objects.all()
    serializer_class = CalculadoraSerializer
    permission_classes = [permissions.IsAuthenticated]