# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-27 20:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblio', '0010_auto_20160520_0829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='fecha_expiracion',
            field=models.DateField(default='2015-05-24'),
        ),
    ]
