# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import lms_backend_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_backend_app', '0021_auto_20151207_2249'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(null=True, upload_to=lms_backend_app.models.get_image_path, blank=True),
        ),
    ]
