# Generated by Django 5.1.2 on 2024-10-22 21:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('detalles', '0001_initial'),
        ('pedidos', '0001_initial'),
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Preparacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(choices=[('En espera', 'En espera'), ('En preparación', 'En preparación'), ('Terminado', 'Terminado')], default='En preparación', max_length=20)),
                ('cantidad', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='detalles.detallepedido')),
                ('pedido', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pedidos.pedido')),
                ('producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='productos.producto')),
            ],
        ),
    ]
