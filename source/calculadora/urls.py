"""calculadora URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers
from calcular import views
from rest_framework_swagger.views import get_swagger_view


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'somas', views.SomaViewSet)
router.register(r'subtracoes', views.SubtracaoViewSet)
router.register(r'multiplicacoes', views.MultiplicacaoViewSet)
router.register(r'divisoes', views.DivisaoViewSet)

schema_view = get_swagger_view(title='API Calculadora')

urlpatterns = [
    url(r'^api/swegger/', schema_view, name='schema_view'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
