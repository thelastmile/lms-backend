# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_backend_app', '0012_auto_20151124_1822'),
    ]

    operations = [
        migrations.RenameField(
            model_name='binarycontent',
            old_name='link',
            new_name='file',
        ),
    ]
