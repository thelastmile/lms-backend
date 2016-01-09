# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('lms_backend_app', '0029_auto_20160108_0747'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodeTestInstructionsJSON',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('json', jsonfield.fields.JSONField(null=True, blank=True)),
                ('code_type', models.ForeignKey(blank=True, to='lms_backend_app.CodeType', null=True)),
                ('module', models.ForeignKey(blank=True, to='lms_backend_app.Module', null=True)),
            ],
        ),
    ]
