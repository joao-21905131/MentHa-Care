# Generated by Django 4.0.3 on 2022-04-19 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diario', '0003_alter_nota_data_alter_nota_grupo_alter_nota_sessao'),
    ]

    operations = [
        migrations.RenameField(
            model_name='participante',
            old_name='data_anscimento',
            new_name='data_nascimento',
        ),
    ]