# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('start_date', models.DateField(auto_now=True)),
                ('end_date', models.DateField()),
                ('paid', models.NullBooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('beds', models.SmallIntegerField(help_text='Number of beds.')),
                ('shared', models.NullBooleanField()),
                ('private', models.NullBooleanField()),
                ('price', models.DecimalField(max_digits=5, decimal_places=2)),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='guest',
            field=models.ForeignKey(to='book.Guest'),
        ),
        migrations.AddField(
            model_name='booking',
            name='room',
            field=models.ForeignKey(to='book.Room'),
        ),
    ]
