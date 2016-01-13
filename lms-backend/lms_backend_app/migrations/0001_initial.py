# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField()),
                ('instructor', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BinaryContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('link', models.FileField(upload_to=b'')),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choices', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CodeType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='CustomContentType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.PositiveIntegerField()),
                ('object_id', models.PositiveIntegerField()),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='FeedbackType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('readme_content', models.TextField()),
                ('course', models.ForeignKey(to='lms_backend_app.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('notes', models.TextField()),
                ('object_id', models.PositiveIntegerField()),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.TextField()),
                ('object_id', models.PositiveIntegerField()),
                ('code_type', models.ForeignKey(to='lms_backend_app.CodeType')),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('model', models.CharField(max_length=256)),
                ('record_id', models.IntegerField()),
                ('tags', models.TextField()),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField()),
                ('question_list_selection', models.ManyToManyField(to='lms_backend_app.Question')),
            ],
        ),
        migrations.CreateModel(
            name='TestResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('instructor', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
                ('question_list_selection', models.ManyToManyField(to='lms_backend_app.Question')),
            ],
        ),
        migrations.CreateModel(
            name='TextContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
                ('lesson', models.ForeignKey(to='lms_backend_app.Lesson')),
            ],
        ),
        migrations.CreateModel(
            name='UnitTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('unit_test', models.TextField()),
                ('code_type', models.ForeignKey(to='lms_backend_app.CodeType')),
                ('question', models.ForeignKey(to='lms_backend_app.Question')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('inmate_id', models.TextField()),
                ('course', models.ForeignKey(to='lms_backend_app.Course')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='testresult',
            name='student',
            field=models.ForeignKey(to='lms_backend_app.UserProfile'),
        ),
        migrations.AddField(
            model_name='testresult',
            name='test',
            field=models.ForeignKey(to='lms_backend_app.Test'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='feedback_type',
            field=models.ForeignKey(to='lms_backend_app.FeedbackType'),
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(to='lms_backend_app.Question'),
        ),
        migrations.AddField(
            model_name='binarycontent',
            name='lesson',
            field=models.ForeignKey(to='lms_backend_app.Lesson'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='student',
            field=models.ForeignKey(to='lms_backend_app.UserProfile'),
        ),
    ]
