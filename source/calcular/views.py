from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from calcular.serializers import UserSerializer
from calcular.serializers import SomaSerializer
from calcular.serializers import SubtracaoSerializer
from calcular.serializers import MultiplicacaoSerializer
from calcular.serializers import DivisaoSerializer
from calcular.models import Soma
from calcular.models import Subtracao 
from calcular.models import Multiplicacao
from calcular.models import Divisao


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class SomaViewSet(viewsets.ModelViewSet):
    queryset = Soma.objects.all()
    serializer_class = SomaSerializer

class SubtracaoViewSet(viewsets.ModelViewSet):
    queryset = Subtracao.objects.all()
    serializer_class = SubtracaoSerializer

class MultiplicacaoViewSet(viewsets.ModelViewSet):
    queryset = Multiplicacao.objects.all()
    serializer_class = MultiplicacaoSerializer

class DivisaoViewSet(viewsets.ModelViewSet):
    queryset = Divisao.objects.all()
    serializer_class = DivisaoSerializer