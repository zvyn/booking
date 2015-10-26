# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20151025_0511'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ('name',)},
        ),
        migrations.AlterField(
            model_name='booking',
            name='end_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='guest',
            field=models.ForeignKey(to='book.Guest', related_name='bookings'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='start_date',
            field=models.DateField(null=True, blank=True),
        ),
    ]
