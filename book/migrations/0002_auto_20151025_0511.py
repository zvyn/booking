# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='paid',
        ),
        migrations.AddField(
            model_name='booking',
            name='paid_until',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='start_date',
            field=models.DateField(),
        ),
    ]
