# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms_backend_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Lesson',
            new_name='Module',
        ),
        migrations.RenameField(
            model_name='binarycontent',
            old_name='lesson',
            new_name='module',
        ),
        migrations.RenameField(
            model_name='textcontent',
            old_name='lesson',
            new_name='module',
        ),
    ]
