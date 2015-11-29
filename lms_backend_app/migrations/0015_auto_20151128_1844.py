# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_backend_app', '0014_auto_20151128_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='binarycontent',
            name='content_type',
            field=models.ForeignKey(to='lms_backend_app.CustomContentType'),
        ),
    ]
