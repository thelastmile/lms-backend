# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_backend_app', '0017_auto_20151129_0801'),
    ]

    operations = [
        migrations.AddField(
            model_name='binarycontent',
            name='extracted_path',
            field=models.CharField(max_length=512, null=True, blank=True),
        ),
    ]
