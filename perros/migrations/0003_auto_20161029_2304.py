# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perros', '0002_persona_perros'),
    ]

    operations = [
        migrations.AddField(
            model_name='perro',
            name='raza',
            field=models.CharField(default=123, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='persona',
            name='apellido',
            field=models.CharField(default=234, max_length=40),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='persona',
            name='dpi',
            field=models.CharField(max_length=13),
        ),
        migrations.AlterField(
            model_name='persona',
            name='nombre',
            field=models.CharField(max_length=40),
        ),
    ]
