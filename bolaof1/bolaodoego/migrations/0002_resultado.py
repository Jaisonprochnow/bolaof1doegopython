# Generated by Django 3.2.5 on 2021-07-12 04:28

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('bolaodoego', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resultado',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('decimo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='res_piloto_10', to='bolaodoego.piloto')),
                ('gp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bolaodoego.gp')),
                ('nono', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='res_piloto_9', to='bolaodoego.piloto')),
                ('oitavo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='res_piloto_8', to='bolaodoego.piloto')),
                ('primeiro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='res_piloto_1', to='bolaodoego.piloto')),
                ('quarto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='res_piloto_4', to='bolaodoego.piloto')),
                ('quinto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='res_piloto_5', to='bolaodoego.piloto')),
                ('segundo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='res_piloto_2', to='bolaodoego.piloto')),
                ('setimo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='res_piloto_7', to='bolaodoego.piloto')),
                ('sexto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='res_piloto_6', to='bolaodoego.piloto')),
                ('terceiro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='res_piloto_3', to='bolaodoego.piloto')),
            ],
            options={
                'db_table': 'resultados',
            },
        ),
    ]
