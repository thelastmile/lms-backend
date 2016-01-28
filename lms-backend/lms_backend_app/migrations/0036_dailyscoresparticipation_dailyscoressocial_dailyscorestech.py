# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lms_backend_app', '0035_auto_20160127_1509'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyScoresParticipation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.PositiveIntegerField(null=True, blank=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('instructor', models.ForeignKey(related_name='instructor_participation', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('student', models.ForeignKey(related_name='_participation', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DailyScoresSocial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.PositiveIntegerField(null=True, blank=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('instructor', models.ForeignKey(related_name='instructor_social', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('student', models.ForeignKey(related_name='student_social', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DailyScoresTech',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.PositiveIntegerField(null=True, blank=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('instructor', models.ForeignKey(related_name='instructor_tech', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('student', models.ForeignKey(related_name='student_tech', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
