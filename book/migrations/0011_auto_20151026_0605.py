# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0010_auto_20151026_0604'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ('name',)},
        ),
        migrations.RemoveField(
            model_name='room',
            name='id',
        ),
        migrations.AddField(
            model_name='room',
            name='name',
            field=models.SlugField(serialize=False, default=9, help_text='Name', max_length=256, primary_key=True),
            preserve_default=False,
        ),
    ]
