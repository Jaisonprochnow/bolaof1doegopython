from datetime import datetime

from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.checks import messages
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PilotoForm, GpForm, Cadastro_usuario, ApostasForm, ResultadosForm
from .models import Piloto, Gp, Aposta, Resultado
from django.contrib import messages
import datetime
from django.core.mail import send_mail

# Create your views here.

def index(request):
    start_date = datetime.date.today()
    end_date = datetime.date(2022, 12, 31)
    corrida = Gp.objects.filter(data_corrida__range=(start_date, end_date))[:3]
    resultado = Resultado.objects.all()
    return render(request, "bolaof1.html", {'corrida': corrida, 'resultado': resultado})

def foto(request):
    return render(request, 'foto.html')

def regulamento(request):
    return render(request, 'regulamento.html')

def cadastro_piloto(request):
    return render(request, 'cadastro_piloto.html')

def cadastro_gp(request):
    return render(request, 'cadastro_gp.html')

def resultados_bolao(request):
    return render(request, 'resultados_bolao.html')

def lista_pilotos(request):
    piloto = Piloto.objects.all()
    return render(request, 'lista_pilotos.html', {'piloto': piloto})

def lista_gps(request):
    piloto = Gp.objects.all()
    return render(request, 'lista_gps.html', {'piloto': piloto})

def lista_apostas(request):
    usuario = request.user
    piloto = Aposta.objects.filter(usuario=usuario)
    dados = {'piloto': piloto}
    return render(request, 'lista_apostas.html', dados)

@login_required
def cadastro_piloto(request):
    form = PilotoForm()
    if(request.method == 'POST'):
        form = PilotoForm(request.POST)
        if(form.is_valid()):
            post_piloto = form.cleaned_data['nome']
            post_numero = form.cleaned_data['numero']
            post_equipe = form.cleaned_data['equipe']
            new_post = Piloto(nome=post_piloto, numero=post_numero, equipe=post_equipe)
            new_post.save()
            messages.add_message(request, messages.INFO, ('Piloto {} cadastrado!').format(post_piloto))
            return redirect('/cadastro_piloto')
        else:
            messages.add_message(request, messages.INFO, 'Piloto ja cadastrado!')
            return redirect('/cadastro_piloto')
    elif(request.method == 'GET'):
        return render(request, 'cadastro_piloto.html', {'form': form})

@login_required
def cadastro_gp(request):
    form = GpForm()
    if(request.method == 'POST'):
        form = GpForm(request.POST)
        if(form.is_valid()):
            post_pais = form.cleaned_data['pais']
            post_circuito = form.cleaned_data['circuito']
            post_data = form.cleaned_data['data_corrida']
            post_hora = form.cleaned_data['hora_corrida']
            new_post = Gp(pais=post_pais, circuito=post_circuito, data_corrida=post_data, hora_corrida=post_hora)
            new_post.save()
            messages.add_message(request, messages.INFO, ('Gp {} cadastrado!').format(post_pais))
            return redirect('/cadastro_gp')
        else:
            messages.add_message(request, messages.INFO, 'GP ja cadastrado!')
            return redirect('/cadastro_gp')

    elif(request.method == 'GET'):
        return render(request, 'cadastro_gp.html', {'form': form})

def cadastrar_usuario(request):
    if request.method == "POST":
        form_usuario = Cadastro_usuario(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('/')
    else:
        form_usuario = Cadastro_usuario()
    return render(request, 'cadastro.html', {'form_usuario': form_usuario})

def logar_usuario(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('index/')
        else:
            messages.add_message(request, messages.INFO, 'Usuario ou senha inválido!')
    else:
        form_login = AuthenticationForm()
    return render(request, 'login.html', {'form_login': form_login})

@login_required
def cadastro_aposta(request):
    form = ApostasForm()
    if(request.method == 'POST'):
        form = ApostasForm(request.POST)
        if not(form.is_valid()):
            post_usuario = request.user
            post_gp = form.cleaned_data['gp']
            post_primeiro = form.cleaned_data['primeiro']
            post_segundo = form.cleaned_data['segundo']
            post_terceiro = form.cleaned_data['terceiro']
            post_quarto = form.cleaned_data['quarto']
            post_quinto = form.cleaned_data['quinto']
            post_sexto = form.cleaned_data['sexto']
            post_setimo = form.cleaned_data['setimo']
            post_oitavo = form.cleaned_data['oitavo']
            post_nono = form.cleaned_data['nono']
            post_decimo = form.cleaned_data['decimo']
            new_post = Aposta(usuario=post_usuario, gp=post_gp, primeiro=post_primeiro, segundo=post_segundo, terceiro=post_terceiro, quarto=post_quarto, quinto=post_quinto, sexto=post_sexto, setimo=post_setimo, oitavo=post_oitavo, nono=post_nono, decimo=post_decimo)
            new_post.save()
            return redirect('/cadastro_apostas')
        else:
            messages.add_message(request, messages.INFO, 'Aposta ja cadastrada!')
            return redirect('/cadastro_apostas')

    elif(request.method == 'GET'):
        return render(request, 'apostas.html', {'form': form})

@login_required
def piloto_update(request, id):
    post = get_object_or_404(Piloto, pk=id)
    form = PilotoForm(instance=post)
    if (request.method == 'POST'):
        form = PilotoForm(request.POST, instance=post)
        if (form.is_valid()):
            post = form.save(commit=False)
            post.piloto = form.cleaned_data['nome']
            post.numero = form.cleaned_data['numero']
            post.equipe = form.cleaned_data['equipe']
            post.save()
            return redirect('/lista_pilotos')
        else:
            return render(request, 'editar_piloto.html', {'form': form, 'post': post})
    elif (request.method == 'GET'):
        return render(request, 'editar_piloto.html', {'form': form, 'post': post})

@login_required
def piloto_delete(request, id):
    post = get_object_or_404(Piloto, pk=id)
    post.delete()
    return render(request, 'excluir_piloto.html')

@login_required
def gp_delete(request, id):
    post = get_object_or_404(Gp, pk=id)
    post.delete()
    return render(request, 'excluir_gp.html')

@login_required
def aposta_delete(request, id):
    post = get_object_or_404(Aposta, pk=id)
    post.delete()
    return render(request, 'excluir_aposta.html')

@login_required
def gp_update(request, id):
    post = get_object_or_404(Gp, pk=id)
    form = GpForm(instance=post)
    if (request.method == 'POST'):
        form = GpForm(request.POST, instance=post)
        if (form.is_valid()):
            post = form.save(commit=False)
            post.pais = form.cleaned_data['pais']
            post.circuito = form.cleaned_data['circuito']
            post.data = form.cleaned_data['data_corrida']
            post.hora = form.cleaned_data['hora_corrida']
            post.save()
            return redirect('/lista_gps')
        else:
            return render(request, 'editar_gp.html', {'form': form, 'post': post})
    elif(request.method == 'GET'):
        return render(request, 'editar_gp.html', {'form': form, 'post': post})


@login_required
def aposta_update(request, id):
    post = get_object_or_404(Aposta, pk=id)
    form = ApostasForm(instance=post)
    if (request.method == 'POST'):
        form = ApostasForm(request.POST, instance=post)
        if (form.is_valid()):
            post = form.save(commit=False)
            post.gp = form.cleaned_data['gp']
            post.primeiro = form.cleaned_data['primeiro']
            post.segundo = form.cleaned_data['segundo']
            post.terceiro = form.cleaned_data['terceiro']
            post.quarto = form.cleaned_data['quarto']
            post.quinto = form.cleaned_data['quinto']
            post.sexto = form.cleaned_data['sexto']
            post.setimo = form.cleaned_data['setimo']
            post.oitavo = form.cleaned_data['oitavo']
            post.nono = form.cleaned_data['nono']
            post.decimo = form.cleaned_data['decimo']
            post.save()

            return redirect('/lista_apostas')
        else:
            return render(request, 'editar_aposta.html', {'form': form, 'post': post})
    elif (request.method == 'GET'):
        return render(request, 'editar_aposta.html', {'form': form, 'post': post})


@login_required
def cadastro_resultado(request):
    form = ResultadosForm()
    form1 = GpForm
    if(request.method == 'POST'):
        form = ResultadosForm(request.POST)
        if (form.is_valid()):
            post_gp = form.cleaned_data['gp']
            post_primeiro = form.cleaned_data['primeiro']
            post_segundo = form.cleaned_data['segundo']
            post_terceiro = form.cleaned_data['terceiro']
            post_quarto = form.cleaned_data['quarto']
            post_quinto = form.cleaned_data['quinto']
            post_sexto = form.cleaned_data['sexto']
            post_setimo = form.cleaned_data['setimo']
            post_oitavo = form.cleaned_data['oitavo']
            post_nono = form.cleaned_data['nono']
            post_decimo = form.cleaned_data['decimo']
            new_post = Resultado(gp=post_gp, primeiro=post_primeiro, segundo=post_segundo, terceiro=post_terceiro, quarto=post_quarto, quinto=post_quinto, sexto=post_sexto, setimo=post_setimo, oitavo=post_oitavo, nono=post_nono, decimo=post_decimo)
            new_post.save()
            messages.add_message(request, messages.INFO, ('Resultado para o {} cadastrado!').format(post_gp))
            return redirect('/cadastro_resultado')
        else:
            messages.add_message(request, messages.INFO, 'Resultado ja cadastrado!')
            return redirect('/cadastro_resultado')

    elif(request.method == 'GET'):
        return render(request, 'cadastro_resultado.html', {'form': form, 'form1': form1})


@login_required
def resultado_update(request, id):
    post = get_object_or_404(Resultado, pk=id)
    form = ResultadosForm(instance=post)
    if (request.method == 'POST'):
        form = ResultadosForm(request.POST, instance=post)
        if not(form.is_valid()):
            post = form.save(commit=False)
            post.gp = form.cleaned_data['gp']
            post.primeiro = form.cleaned_data['primeiro']
            post.segundo = form.cleaned_data['segundo']
            post.terceiro = form.cleaned_data['terceiro']
            post.quarto = form.cleaned_data['quarto']
            post.quinto = form.cleaned_data['quinto']
            post.sexto = form.cleaned_data['sexto']
            post.setimo = form.cleaned_data['setimo']
            post.oitavo = form.cleaned_data['oitavo']
            post.nono = form.cleaned_data['nono']
            post.decimo = form.cleaned_data['decimo']
            post.save()
            return redirect('/lista_resultados')
        else:
            return render(request, 'editar_resultado.html', {'form': form, 'post': post})
    elif (request.method == 'GET'):
        return render(request, 'editar_resultado.html', {'form': form, 'post': post})

@login_required
def resultado_delete(request, id):
    post = get_object_or_404(Resultado, pk=id)
    post.delete()
    return render(request, 'excluir_resultado.html')

def lista_resultados(request):
    piloto = Resultado.objects.all()
    return render(request, 'lista_resultado.html', {'piloto': piloto})

def lista_resultados_2(request):
    piloto = Resultado.objects.all()
    return render(request, 'lista_resultado_2.html', {'piloto': piloto})


