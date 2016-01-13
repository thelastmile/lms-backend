# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('lms_backend_app', '0002_auto_20150930_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='instructor',
            field=models.ForeignKey(related_name='instructor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='student',
            field=models.ForeignKey(related_name='student', to=settings.AUTH_USER_MODEL),
        ),
    ]
