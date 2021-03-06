# Generated by Django 4.0.3 on 2022-07-11 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diario', '0031_alter_exercicio_sessao'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercicio',
            name='duracao',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='exercicio',
            name='fase',
            field=models.CharField(blank=True, choices=[('I', 'Inicial'), ('D', 'Desenvolvimento'), ('F', 'Final')], max_length=10, null=True),
        ),
    ]
