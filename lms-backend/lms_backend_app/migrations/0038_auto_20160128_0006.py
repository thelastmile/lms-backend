# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_backend_app', '0037_note_instructor_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='content_type',
            field=models.ForeignKey(blank=True, to='contenttypes.ContentType', null=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='object_id',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
    ]
