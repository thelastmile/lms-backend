# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_backend_app', '0019_auto_20151205_1148'),
    ]

    operations = [
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('code', models.TextField(null=True, blank=True)),
                ('html', models.TextField(null=True, blank=True)),
                ('css', models.TextField(null=True, blank=True)),
                ('tests', models.TextField(null=True, blank=True)),
                ('code_type', models.ForeignKey(blank=True, to='lms_backend_app.CodeType', null=True)),
            ],
        ),
    ]
