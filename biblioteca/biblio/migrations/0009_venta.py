# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-20 14:23
from __future__ import unicode_literals

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblio', '0008_auto_20160519_2327'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now=True)),
                ('total', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=8)),
                ('titulo', models.CharField(max_length=39)),
                ('titulo', models.CharField(max_length=39)),
                ('tarjeta', models.CharField(max_length=39)),
                ('fecha_expiracion', models.DateField()),
                ('direccion', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
