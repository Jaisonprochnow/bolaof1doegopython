"""Bolaof1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import RedirectView
from bolaodoego import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('foto/', views.foto),
    path('', RedirectView.as_view(url='index/')),
    path('regulamento/', views.regulamento),
    path('account/', include('django.contrib.auth.urls')),
    path('cadastro_piloto/', views.cadastro_piloto, name='cadastro_piloto'),
    path('cadastro_gp/', views.cadastro_gp, name='cadastro_gp'),
    path('lista_pilotos/', views.lista_pilotos),
    path('lista_gps/', views.lista_gps),
    path('cadastar_usuario/', views.cadastrar_usuario, name='cadastrar_usuario'),
    path('cadastro_apostas/', views.cadastro_aposta, name='cadastro_apostas'),
    path('lista_apostas/', views.lista_apostas, name='lista_apostas'),
    path('lista_pilotos/editar/<str:id>/', views.piloto_update),
    path('lista_pilotos/deletar/<str:id>/', views.piloto_delete),
    path('lista_gps/editar/<str:id>/', views.gp_update),
    path('lista_gps/deletar/<str:id>/', views.gp_delete),
    path('lista_apostas/deletar/<str:id>/', views.aposta_delete),
    path('lista_apostas/editar/<str:id>/', views.aposta_update),
    path('cadastro_resultado/', views.cadastro_resultado, name='cadastro_resultado'),
    path('lista_resultado/', views.lista_resultados, name='lista_resultados'),
    path('lista_resultado_2/', views.lista_resultados_2, name='lista_resultados_2'),
    path('lista_resultado/deletar/<str:id>/', views.resultado_delete),
    path('lista_resultado/editar/<str:id>/', views.resultado_update),
    path('resultados_bolao', views.resultados_bolao, name='resultados_bolao'),

]
