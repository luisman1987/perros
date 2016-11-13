# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perros', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='perros',
            field=models.ManyToManyField(to='perros.Perro', through='perros.PP'),
        ),
    ]
