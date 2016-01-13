# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_backend_app', '0009_auto_20151117_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='attendance',
            field=models.NullBooleanField(choices=[(None, b'Student Not Present'), (True, b'Student Present Full Class Time'), (False, b'Student Present Partial Class Time')]),
        ),
    ]
