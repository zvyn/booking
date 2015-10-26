# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0007_auto_20151026_0517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='name',
            field=models.SlugField(serialize=False, unique=True, primary_key=True, max_length=256),
        ),
    ]
