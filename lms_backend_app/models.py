from django.contrib.auth.models import User
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models


# Create your models here.

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

    def __unicode__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    course = models.ForeignKey(Course)
    inmate_id = models.TextField()

    def __unicode__(self):
        return self.user.first_name

class Attendance(models.Model):
    student = models.ForeignKey(User, related_name='student')
    instructor = models.ForeignKey(User, related_name='instructor')
    date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s %s' % (self.student, self.date)


class CustomContentType(models.Model):
    name = models.CharField(max_length=128)
    # (ex, video, audio, text, README, Markdown etc)
    def __unicode__(self):
        return self.name


class CodeType(models.Model):
    name = models.CharField(max_length=256)

    def __unicode__(self):
        return self.name


class Question(models.Model):
    # can pertain to a module or test
    question = models.TextField()
    code_type = models.ForeignKey(CodeType)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    def __unicode__(self):
        return self.question

class Note(models.Model):
    # Agnostic Notes encompassing Faculty and Student notes with many content types
    author = models.ForeignKey(User)
    title = models.CharField(max_length=256)
    body = models.TextField()
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    def __unicode__(self):
        return self.title


class FeedbackType(models.Model):
    name = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name


class Feedback(models.Model):
    # Agnostic feedback
    #TODO NEEDS ATTENTION: HOOK UP TO AUTHOR AND STUDENT
    author = models.ForeignKey(User, related_name='feedback_author')
    student = models.ForeignKey(User, related_name='feedback_student')
    rating = models.PositiveIntegerField()  # 1 - 10 numeric (10 best, 1 worst)
    feedback_type = models.ForeignKey(FeedbackType)
    content_type = models.ForeignKey(ContentType, blank=True, null=True)
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    def __unicode__(self):
        return '%s %d' % (self.author, self.rating)


class Module(models.Model):
    name = models.CharField(max_length=128)
    readme_content = models.TextField()
    course = models.ForeignKey(Course)

    def __unicode__(self):
        return self.name


class BinaryContent(models.Model):
    content_type = models.ForeignKey(ContentType, default='BinaryContent')
    link = models.FileField()
    module = models.ForeignKey(Module)

    def __unicode__(self):
        return self.content_type


class TextContent(models.Model):
    # (This is where the markdown will live. Increased to fit large lessons)
    content_type = models.ForeignKey(ContentType)
    text = models.TextField()
    module = models.ForeignKey(Module)

    def __unicode__(self):
        return self.content_type


class Test(models.Model):
    question_list_selection = models.ManyToManyField(Question)
    created = models.DateTimeField(auto_created=True)

    def __unicode__(self):
        return self.question_list_selection


class UnitTest(models.Model):
    unit_test = models.TextField()
    question = models.ForeignKey(Question)
    code_type = models.ForeignKey(CodeType)

    def __unicode__(self):
        return self.unit_test


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choices = models.TextField()

    def __unicode__(self):
        return '%s : %s' % (self.question, self.choices)


class TestResult(models.Model):
    score = models.IntegerField(default=0)
    test = models.ForeignKey(Test)
    student = models.ForeignKey(UserProfile)
    instructor = models.OneToOneField(User, primary_key= False)
    question_list_selection = models.ManyToManyField(Question)

    def __unicode__(self):
        return self.score


class Tag(models.Model):
    model = models.CharField(max_length=256)
    record_id = models.IntegerField()
    tags = models.TextField()
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    def __unicode__(self):
        return self.tags