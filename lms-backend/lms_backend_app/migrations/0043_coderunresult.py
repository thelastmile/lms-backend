# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lms_backend_app', '0042_homepagecontent'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodeRunResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.TextField(null=True, blank=True)),
                ('tests', models.TextField(null=True, blank=True)),
                ('status', models.CharField(blank=True, max_length=4, null=True, choices=[(b'PASS', b'PASS'), (b'FAIL', b'FAIL')])),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('problem_name', models.CharField(max_length=256)),
                ('course', models.ForeignKey(blank=True, to='lms_backend_app.Course', null=True)),
                ('module', models.ForeignKey(blank=True, to='lms_backend_app.Module', null=True)),
                ('problem_link', models.ForeignKey(to='lms_backend_app.CodeTestInstructionsJSON')),
                ('student', models.ForeignKey(to='lms_backend_app.UserProfile')),
            ],
        ),
    ]
