# Generated by Django 4.0.3 on 2022-06-01 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diario', '0013_presenca_faltou'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='presenca',
            name='present',
        ),
    ]
