# Generated by Django 4.0.3 on 2022-07-14 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diario', '0043_alter_sessao_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercicio',
            name='materiais',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
