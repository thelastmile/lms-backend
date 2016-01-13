# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import lms_backend_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_backend_app', '0025_setting'),
    ]

    operations = [
        migrations.AddField(
            model_name='binarycontent',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to=lms_backend_app.models.get_content_tn_path, blank=True),
        ),
    ]
