# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0008_auto_20151026_0526'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guest',
            old_name='noted',
            new_name='note',
        ),
    ]
