# Generated by Django 4.0.3 on 2022-07-14 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diario', '0042_alter_exercicio_atividade_alter_exercicio_objetivo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sessao',
            name='nome',
            field=models.CharField(max_length=100),
        ),
    ]