# Generated by Django 4.0.3 on 2022-06-01 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diario', '0014_remove_presenca_present'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presenca',
            name='faltou',
            field=models.BooleanField(blank=True),
        ),
    ]