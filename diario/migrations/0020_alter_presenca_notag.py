# Generated by Django 4.0.3 on 2022-06-13 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diario', '0019_alter_presenca_notag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presenca',
            name='notaG',
            field=models.TextField(default=False),
        ),
    ]
