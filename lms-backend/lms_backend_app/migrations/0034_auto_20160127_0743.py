# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lms_backend_app', '0033_accesslog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accesslog',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
