# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_backend_app', '0040_binarycontent_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='order',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
