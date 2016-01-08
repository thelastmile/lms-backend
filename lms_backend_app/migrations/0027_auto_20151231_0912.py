# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_backend_app', '0026_binarycontent_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='binarycontent',
            name='is_global',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='binarycontent',
            name='module',
            field=models.ForeignKey(blank=True, to='lms_backend_app.Module', null=True),
        ),
    ]
