# Generated by Django 4.0.3 on 2022-07-15 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diario', '0044_alter_exercicio_materiais'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notagrupo',
            name='grupo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='diario.grupocare'),
        ),
    ]