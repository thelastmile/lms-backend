# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_backend_app', '0039_binarycontent_index_file_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='binarycontent',
            name='order',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
