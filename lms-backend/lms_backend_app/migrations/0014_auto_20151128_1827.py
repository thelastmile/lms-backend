# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import lms_backend_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_backend_app', '0013_auto_20151128_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='binarycontent',
            name='content_type',
            field=models.ForeignKey(to='contenttypes.ContentType'),
        ),
        migrations.AlterField(
            model_name='binarycontent',
            name='file',
            field=models.FileField(upload_to=lms_backend_app.models.upload_job_file_path),
        ),
    ]
