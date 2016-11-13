# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perros', '0004_perro_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='foto',
            field=models.FileField(upload_to='', null=True, blank=True),
        ),
    ]
