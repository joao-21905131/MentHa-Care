# Generated by Django 4.0.3 on 2022-06-13 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diario', '0017_alter_presenca_faltou_alter_presenca_present'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notagrupo',
            old_name='nota',
            new_name='notaG',
        ),
        migrations.RenameField(
            model_name='presenca',
            old_name='nota',
            new_name='notaG',
        ),
    ]
