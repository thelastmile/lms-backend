from django.contrib.auth.models import User
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models

# Create your models here.
from django.db.models import ForeignKey

"""
NOTE: the usage of the following allows ForeignKey model associations to ANY model:

Agnostic

content_type = models.ForeignKey(CustomContentType)
object_id = models.PositiveIntegerField()
content_object = generic.GenericForeignKey('content_type', 'object_id')

This will be used for items like notes and tags, where the note or tag could pertain to several different types of objects.  This allows an unlimited number of object types to associate with.

from django.db import models
GOING TO USE DJANGO USER GROUPS FOR THE BASE USER MODEL - this is why you don't see any references to user groups or user types.  It's a Django freebie.  Includes First Name, Last Name
"""


class Course(models.Model):
    name = models.CharField(max_length=128)


class UserProfile(models.Model):
    user = models.ForeignKey(User)
    course = models.ForeignKey(Course)
    inmate_id = models.TextField()


class Attendance(models.Model):
    student = models.ForeignKey(User)
    teacher = models.ForeignKey(User)
    date = models.DateTimeField()


class CustomContentType(models.Model):
    name = models.CharField(max_length=128)
    # (ex, video, audio, text, README, Markdown etc)


class FeedbackType(models.Model):
    name = models.CharField(max_length=128)


class CodeType(models.Model):
    name = models.CharField(max_length=256)


class Question(models.Model):
    # for a test or an item on a lesson
    question = models.TextField()
    code_type = ForeignKey(CodeType)
    # make relatable to Test or a Lesson
    content_type = models.ForeignKey(CustomContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')


class Note(models.Model):
    # Agnostic Notes encompassing Faculty and Student notes with many content types
    author = models.ForeignKey(User)
    notes = models.TextField()
    content_type = models.ForeignKey(CustomContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')


class Feedback(models.Model):
    # Agnostic feedback
    author = models.ForeignKey(User)
    rating = models.PositiveIntegerField(max_length=10)  # 1 - 10 numeric (10 best, 1 worst)
    feedback_type = models.ForeignKey(FeedbackType)
    content_type = models.ForeignKey(CustomContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')


class Lesson(models.Model):
    name = models.CharField(max_length=128)
    readme_content = models.TextField()
    course = models.ForeignKey(Course)


class BinaryContent(models.Model):
    content_type = models.ForeignKey(CustomContentType)
    link = models.FileField()
    lesson = models.ForeignKey(Lesson)


class TextContent(models.Model):
    content_type = models.ForeignKey(CustomContentType)
    text = models.TextField()
    # (This is where the markdown will live. Increased to fit large lessons)
    lesson = models.ForeignKey(Lesson)


class Test(models.Model):
    question_list_selection = models.ManyToManyField(Question)
    created = models.DateTimeField()


class UnitTest(models.Model):
    unit_test = models.TextField()
    question = models.ForeignKey(Question)
    code_type = models.ForeignKey(CodeType)


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choices = models.TextField()


class TestResult(models.Model):
    test = models.ForeignKey(Test)
    student = models.ForeignKey(User)
    teacher = models.ForeignKey(User)
    question_list_selection = models.ManyToManyField(Question)


class Tag(models.Model):
    model = models.CharField(256)
    record_id = models.IntegerField(max_length=2)
    tags = models.TextField()
    content_type = models.ForeignKey(CustomContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')
