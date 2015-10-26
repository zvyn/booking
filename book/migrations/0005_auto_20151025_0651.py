# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_auto_20151025_0619'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ('slug',)},
        ),
        migrations.RemoveField(
            model_name='room',
            name='name',
        ),
        migrations.AddField(
            model_name='room',
            name='slug',
            field=models.SlugField(max_length=256, default=9),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='room',
            name='private',
            field=models.BooleanField(default=False),
        ),
    ]
