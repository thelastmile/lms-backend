# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lms_backend_app', '0005_auto_20151001_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='student',
            field=models.ForeignKey(related_name='feedback_student', default='', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='binarycontent',
            name='content_type',
            field=models.ForeignKey(to='contenttypes.ContentType', null=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='author',
            field=models.ForeignKey(related_name='feedback_author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='content_type',
            field=models.ForeignKey(to='contenttypes.ContentType', null=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='object_id',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
