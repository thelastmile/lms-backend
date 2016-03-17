# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_backend_app', '0041_module_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePageContent',
            fields=[
                ('course', models.OneToOneField(primary_key=True, serialize=False, to='lms_backend_app.Course')),
                ('content', models.TextField(null=True, blank=True)),
            ],
        ),
    ]
