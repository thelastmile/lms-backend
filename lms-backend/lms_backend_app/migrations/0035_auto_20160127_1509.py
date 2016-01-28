# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('lms_backend_app', '0034_auto_20160127_0743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='instructor',
            field=models.ForeignKey(related_name='instructor', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
