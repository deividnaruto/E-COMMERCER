# Generated by Django 4.1.6 on 2023-03-01 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_remove_perfil_usuario_senha'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='perfil_usuario',
            options={'verbose_name': 'Perfil Usuario', 'verbose_name_plural': 'Perfils de Usuarios'},
        ),
    ]
