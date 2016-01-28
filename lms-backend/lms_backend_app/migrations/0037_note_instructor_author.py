# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lms_backend_app', '0036_dailyscoresparticipation_dailyscoressocial_dailyscorestech'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='instructor_author',
            field=models.ForeignKey(related_name='note_instructor_author', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
