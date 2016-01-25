# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_backend_app', '0030_codetestinstructionsjson'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='codetestinstructionsjson',
            options={'verbose_name': 'JSON Test with Instructions', 'verbose_name_plural': 'JSON Tests with Instructions'},
        ),
    ]
