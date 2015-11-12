# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_backend_app', '0007_auto_20151105_0246'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='notes',
            new_name='body',
        ),
        migrations.AddField(
            model_name='note',
            name='title',
            field=models.CharField(default='', max_length=256),
            preserve_default=False,
        ),
    ]
