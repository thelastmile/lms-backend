# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_backend_app', '0011_auto_20151124_2018'),
    ]

    operations = [
        migrations.RenameField(
            model_name='module',
            old_name='readme_content',
            new_name='description',
        ),
    ]
