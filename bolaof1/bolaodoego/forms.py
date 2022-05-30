from django import forms
from django.contrib.auth.forms import UserCreationForm


from .models import *

class PilotoForm(forms.ModelForm):
    class Meta:
        model = Piloto
        fields = ["nome", "numero", "equipe"]

class GpForm(forms.ModelForm):
    class Meta:
        model = Gp
        fields = ["pais", "circuito", "data_corrida", "hora_corrida"]

class Cadastro_usuario(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1','password2')

class ApostasForm(forms.ModelForm):
    class Meta:
        model = Aposta
        fields = ["usuario", "gp", "primeiro", "segundo", "terceiro", "quarto", "quinto", "sexto", "setimo", "oitavo", "nono", "decimo"]

class ResultadosForm(forms.ModelForm):
    class Meta:
        model = Resultado
        fields = ["gp", "primeiro", "segundo", "terceiro", "quarto", "quinto", "sexto", "setimo",
                  "oitavo", "nono", "decimo"]
