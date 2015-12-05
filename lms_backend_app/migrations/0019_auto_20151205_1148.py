# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_backend_app', '0018_binarycontent_extracted_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='course',
            field=models.ForeignKey(blank=True, to='lms_backend_app.Course', null=True),
        ),
    ]
