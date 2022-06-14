# Generated by Django 4.0.3 on 2022-05-25 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diario', '0009_respostas_informacoes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Presenca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('present', models.BooleanField()),
                ('mode', models.CharField(blank=True, choices=[('L', 'Presencial'), ('O', 'Online')], max_length=20, null=True)),
                ('withApp', models.BooleanField(blank=True, null=True)),
                ('participante', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='presencas', to='diario.participante')),
                ('sessao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sessao', to='diario.sessao')),
            ],
        ),
        migrations.CreateModel(
            name='PartilhaGrupo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partilha', models.TextField()),
                ('data', models.DateTimeField(auto_now_add=True, null=True)),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diario.grupocare')),
            ],
        ),
        migrations.CreateModel(
            name='NotaGrupo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.TextField()),
                ('data', models.DateTimeField(auto_now_add=True, null=True)),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diario.grupocare')),
            ],
        ),
    ]