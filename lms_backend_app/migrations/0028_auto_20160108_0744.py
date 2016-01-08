# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_backend_app', '0027_auto_20151231_0912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='value',
            field=models.TextField(null=True, blank=True),
        ),
    ]
