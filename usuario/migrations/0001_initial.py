# Generated by Django 4.1.6 on 2023-02-13 21:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil_Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('sobrenome', models.CharField(max_length=150)),
                ('data_de_nascimento', models.CharField(max_length=8)),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.CharField(max_length=11)),
                ('cpf', models.CharField(max_length=11)),
                ('senha', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
