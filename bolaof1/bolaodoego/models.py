import uuid
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Piloto(models.Model):
    nome = models.CharField(primary_key=True, max_length=15, blank=False, null=False)
    numero = models.IntegerField(blank=False, null=False)
    equipe = models.CharField(max_length=15, blank=False, null=False)

    class Meta:
        db_table = 'pilotos'

    def __str__(self):
        return self.nome


class Gp(models.Model):
    pais = models.CharField(primary_key=True, max_length=50, blank=False, null=False)
    circuito = models.CharField(max_length=50, blank=False, null=False)
    data_corrida = models.DateField(blank=False, verbose_name='Data da corrida')
    hora_corrida = models.TimeField(blank=False, verbose_name='hora da corrida')
    class Meta:
        db_table = 'gps'

    def __str__(self):
        return self.pais

class Aposta(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    gp = models.ForeignKey(Gp, on_delete=models.CASCADE)
    primeiro = models.ForeignKey(Piloto, related_name='piloto_1', on_delete=models.CASCADE)
    segundo = models.ForeignKey(Piloto, related_name='piloto_2', on_delete=models.CASCADE)
    terceiro = models.ForeignKey(Piloto, related_name='piloto_3', on_delete=models.CASCADE)
    quarto = models.ForeignKey(Piloto, related_name='piloto_4',on_delete=models.CASCADE)
    quinto = models.ForeignKey(Piloto, related_name='piloto_5',on_delete=models.CASCADE)
    sexto = models.ForeignKey(Piloto, related_name='piloto_6',on_delete=models.CASCADE)
    setimo = models.ForeignKey(Piloto, related_name='piloto_7',on_delete=models.CASCADE)
    oitavo = models.ForeignKey(Piloto, related_name='piloto_8',on_delete=models.CASCADE)
    nono = models.ForeignKey(Piloto, related_name='piloto_9',on_delete=models.CASCADE)
    decimo = models.ForeignKey(Piloto, related_name='piloto_10',on_delete=models.CASCADE)

    class Meta:
        db_table = 'apostas'


class Resultado(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    gp = models.ForeignKey(Gp, on_delete=models.CASCADE)
    primeiro = models.ForeignKey(Piloto, related_name='res_piloto_1', on_delete=models.CASCADE)
    segundo = models.ForeignKey(Piloto, related_name='res_piloto_2', on_delete=models.CASCADE)
    terceiro = models.ForeignKey(Piloto, related_name='res_piloto_3', on_delete=models.CASCADE)
    quarto = models.ForeignKey(Piloto, related_name='res_piloto_4',on_delete=models.CASCADE)
    quinto = models.ForeignKey(Piloto, related_name='res_piloto_5',on_delete=models.CASCADE)
    sexto = models.ForeignKey(Piloto, related_name='res_piloto_6',on_delete=models.CASCADE)
    setimo = models.ForeignKey(Piloto, related_name='res_piloto_7',on_delete=models.CASCADE)
    oitavo = models.ForeignKey(Piloto, related_name='res_piloto_8',on_delete=models.CASCADE)
    nono = models.ForeignKey(Piloto, related_name='res_piloto_9',on_delete=models.CASCADE)
    decimo = models.ForeignKey(Piloto, related_name='res_piloto_10',on_delete=models.CASCADE)

    class Meta:
        db_table = 'resultados'


