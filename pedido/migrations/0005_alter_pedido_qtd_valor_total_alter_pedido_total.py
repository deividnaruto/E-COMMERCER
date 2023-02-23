# Generated by Django 4.1.6 on 2023-02-23 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0004_itempedido_slug_alter_pedido_qtd_valor_total_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='qtd_valor_total',
            field=models.FloatField(max_length=300, verbose_name='Valor Total'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='total',
            field=models.PositiveIntegerField(verbose_name='Total de Produtos'),
        ),
    ]
