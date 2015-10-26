# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_auto_20151026_0453'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='guest',
            name='noted',
            field=models.TextField(max_length=2048, blank=True),
        ),
    ]
