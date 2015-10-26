# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_auto_20151025_0611'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='price',
            new_name='price_per_day',
        ),
        migrations.AddField(
            model_name='room',
            name='price_per_week',
            field=models.DecimalField(decimal_places=2, default=175, max_digits=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='room',
            name='private',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='room',
            name='shared',
            field=models.BooleanField(default=True),
        ),
    ]
