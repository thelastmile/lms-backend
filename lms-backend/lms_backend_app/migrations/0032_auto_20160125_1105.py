# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import lms_backend_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_backend_app', '0031_auto_20160125_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='binarycontent',
            name='file',
            field=models.FileField(max_length=256, upload_to=lms_backend_app.models.upload_job_file_path),
        ),
        migrations.AlterField(
            model_name='binarycontent',
            name='thumbnail',
            field=models.ImageField(max_length=256, null=True, upload_to=lms_backend_app.models.get_content_tn_path, blank=True),
        ),
    ]
