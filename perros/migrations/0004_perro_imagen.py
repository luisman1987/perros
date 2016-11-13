# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perros', '0003_auto_20161029_2304'),
    ]

    operations = [
        migrations.AddField(
            model_name='perro',
            name='imagen',
            field=models.FileField(upload_to='', null=True, blank=True),
        ),
    ]
