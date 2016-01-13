# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms_backend_app', '0003_auto_20150930_2332'),
    ]

    operations = [
        migrations.AddField(
            model_name='testresult',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
