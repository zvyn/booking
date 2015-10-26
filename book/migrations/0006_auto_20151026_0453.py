# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_auto_20151025_0651'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guest',
            name='id',
        ),
        migrations.AddField(
            model_name='guest',
            name='noted',
            field=models.TextField(max_length=2048, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='guest',
            name='name',
            field=models.CharField(serialize=False, unique=True, primary_key=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='room',
            name='slug',
            field=models.SlugField(help_text='Name', max_length=256),
        ),
    ]
