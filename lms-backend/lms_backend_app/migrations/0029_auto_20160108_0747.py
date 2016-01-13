# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_backend_app', '0028_auto_20160108_0744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='name',
            field=models.CharField(unique=True, max_length=50),
        ),
    ]
