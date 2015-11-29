# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_backend_app', '0016_course_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='binarycontent',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='binarycontent',
            name='index_file',
            field=models.CharField(max_length=256, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='binarycontent',
            name='name',
            field=models.CharField(default='', max_length=256),
            preserve_default=False,
        ),
    ]
