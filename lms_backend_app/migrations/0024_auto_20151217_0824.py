# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lms_backend_app', '0023_auto_20151208_0914'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='testresult',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
