from django.contrib import admin
from .models import Piloto, Gp, Aposta, Resultado

# Register your models here.


class PilotoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'numero', 'equipe')

admin.site.register(Piloto, PilotoAdmin)

class GpAdmin(admin.ModelAdmin):
    list_display = ('pais', 'circuito', 'data_corrida', 'hora_corrida')

admin.site.register(Gp, GpAdmin)

@admin.register(Aposta)
class ApostaAdmin(admin.ModelAdmin):
    model = Aposta
    list_display = ['usuario', 'get_pais', 'get_nome1', 'get_nome2', 'get_nome3', 'get_nome4', 'get_nome5', 'get_nome6', 'get_nome7', 'get_nome8', 'get_nome9', 'get_nome10']
    list_filter = ['usuario']


    def get_pais(self, obj):
        return obj.gp.pais
    get_pais.admin_order_field = 'gp'
    get_pais.short_description = 'Gp'

    def get_nome1(self, obj):
        return obj.primeiro.nome
    get_nome1.admin_order_field = 'piloto'
    get_nome1.short_description = '1º'

    def get_nome2(self, obj):
        return obj.segundo.nome
    get_nome2.admin_order_field = 'piloto'
    get_nome2.short_description = '2º'

    def get_nome3(self, obj):
        return obj.terceiro.nome
    get_nome3.admin_order_field = 'piloto'
    get_nome3.short_description = '3º'

    def get_nome4(self, obj):
        return obj.quarto.nome
    get_nome4.admin_order_field = 'piloto'
    get_nome4.short_description = '4º'

    def get_nome5(self, obj):
        return obj.quinto.nome
    get_nome5.admin_order_field = 'piloto'
    get_nome5.short_description = '5º'

    def get_nome6(self, obj):
        return obj.sexto.nome
    get_nome6.admin_order_field = 'piloto'
    get_nome6.short_description = '6º'

    def get_nome7(self, obj):
        return obj.setimo.nome
    get_nome7.admin_order_field = 'piloto'
    get_nome7.short_description = '7º'

    def get_nome8(self, obj):
        return obj.oitavo.nome
    get_nome8.admin_order_field = 'piloto'
    get_nome8.short_description = '8º'

    def get_nome9(self, obj):
        return obj.nono.nome
    get_nome9.admin_order_field = 'piloto'
    get_nome9.short_description = '9º'

    def get_nome10(self, obj):
        return obj.decimo.nome
    get_nome10.admin_order_field = 'piloto'
    get_nome10.short_description = '10º'


@admin.register(Resultado)
class ResultadoAdmin(admin.ModelAdmin):
    model = Aposta
    list_display = ['get_pais', 'get_nome1', 'get_nome2', 'get_nome3', 'get_nome4', 'get_nome5', 'get_nome6', 'get_nome7', 'get_nome8', 'get_nome9', 'get_nome10']
    list_filter = ['gp']

    def get_pais(self, obj):
        return obj.gp.pais

    get_pais.admin_order_field = 'gp'
    get_pais.short_description = 'Gp'

    def get_nome1(self, obj):
        return obj.primeiro.nome

    get_nome1.admin_order_field = 'piloto'
    get_nome1.short_description = '1º'

    def get_nome2(self, obj):
        return obj.segundo.nome

    get_nome2.admin_order_field = 'piloto'
    get_nome2.short_description = '2º'

    def get_nome3(self, obj):
        return obj.terceiro.nome

    get_nome3.admin_order_field = 'piloto'
    get_nome3.short_description = '3º'

    def get_nome4(self, obj):
        return obj.quarto.nome

    get_nome4.admin_order_field = 'piloto'
    get_nome4.short_description = '4º'

    def get_nome5(self, obj):
        return obj.quinto.nome

    get_nome5.admin_order_field = 'piloto'
    get_nome5.short_description = '5º'

    def get_nome6(self, obj):
        return obj.sexto.nome

    get_nome6.admin_order_field = 'piloto'
    get_nome6.short_description = '6º'

    def get_nome7(self, obj):
        return obj.setimo.nome

    get_nome7.admin_order_field = 'piloto'
    get_nome7.short_description = '7º'

    def get_nome8(self, obj):
        return obj.oitavo.nome

    get_nome8.admin_order_field = 'piloto'
    get_nome8.short_description = '8º'

    def get_nome9(self, obj):
        return obj.nono.nome

    get_nome9.admin_order_field = 'piloto'
    get_nome9.short_description = '9º'

    def get_nome10(self, obj):
        return obj.decimo.nome

    get_nome10.admin_order_field = 'piloto'
    get_nome10.short_description = '10º'