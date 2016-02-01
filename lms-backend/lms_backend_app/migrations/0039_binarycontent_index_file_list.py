# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('lms_backend_app', '0038_auto_20160128_0006'),
    ]

    operations = [
        migrations.AddField(
            model_name='binarycontent',
            name='index_file_list',
            field=jsonfield.fields.JSONField(null=True, blank=True),
        ),
    ]
