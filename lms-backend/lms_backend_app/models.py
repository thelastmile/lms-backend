from django.contrib.auth.models import User
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models
from lmsbackend import settings
import uuid
import zipfile
import os
from django.utils import timezone
from jsonfield import JSONField

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
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name

class Module(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    course = models.ForeignKey(Course)

    def __unicode__(self):
        return self.name

def get_image_path(instance, filename):
    return os.path.join(settings.MEDIA_PHOTOS, str(instance.id), filename)

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    course = models.ForeignKey(Course, blank=True, null=True)
    profile_image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    inmate_id = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return '%s %s' % (self.user.first_name,self.user.last_name)

ATTENDANCE_CHOICES = (
    (None, "Student Not Present"),
    (True, "Student Present Full Class Time"),
    (False, "Student Present Partial Class Time")
)

class Attendance(models.Model):
    student = models.ForeignKey(User, related_name='student')
    instructor = models.ForeignKey(User, related_name='instructor')
    attendance = models.NullBooleanField(choices = ATTENDANCE_CHOICES)
    date = models.DateTimeField(default=timezone.now)

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

class Code(models.Model):
    student = models.ForeignKey(User)
    name = models.CharField(max_length=256)
    code = models.TextField(blank=True, null=True)
    html = models.TextField(blank=True, null=True)
    css = models.TextField(blank=True, null=True)
    tests = models.TextField(blank=True, null=True)
    code_type = models.ForeignKey(CodeType,blank=True, null=True)
    module = models.ForeignKey(Module, blank=True, null=True)

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
    title = models.CharField(max_length=256,blank=True, null=True)
    body = models.TextField()
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    date = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return "%s %s %s %s" % (self.date,self.author.first_name,self.author.last_name,self.title)


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

def upload_job_file_path(instance, filename):
    ext = filename.split(".")[-1].lower()
    # change the filename to guid
    filename = '%s.%s' % (uuid.uuid4(),ext)
    if ext == 'pdf':
        return '%s%s' % (settings.MEDIA_PDF, filename)

    if ext == 'html' or ext == 'htm' :
        return '%s%s' % (settings.MEDIA_HTML, filename)

    if ext == 'jpg' or ext == 'png' or ext == 'jpeg' or ext == 'svg':
        return '%s%s' % (settings.MEDIA_IMG, filename)

    if ext == 'mp4' or ext == 'mpg' or ext == 'mkv' or ext == 'avi':
        return '%s%s' % (settings.MEDIA_VIDEO, filename)

    return '%s%s' % (settings.MEDIA_MISC, filename)


def get_content_tn_path(instance, filename):
    return os.path.join(settings.MEDIA_CONTENT_THUMBNAILS, str(instance.id), filename)

class BinaryContent(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey(CustomContentType)
    file = models.FileField(max_length=256,upload_to=upload_job_file_path)
    module = models.ForeignKey(Module,blank=True, null=True)
    is_global = models.NullBooleanField();
    index_file = models.CharField(max_length=256,blank=True, null=True)
    extracted_path = models.CharField(max_length=512,blank=True, null=True)
    thumbnail = models.ImageField(max_length=256,upload_to=get_content_tn_path, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.pk is None:
            ext = self.file.name.split(".")[-1].lower()
            directoryname = '%s' % (uuid.uuid4())
            if ext.lower() == 'zip':
                zfile = zipfile.ZipFile(self.file)
                self.extracted_path = '%s%s/' % (settings.MEDIA_MISC, directoryname)
                self.full_extracted_path = '%s%s' % (settings.MEDIA_ROOT,self.extracted_path)
                zfile.extractall(self.full_extracted_path)
        super(BinaryContent, self).save(*args, **kwargs) # Call the "real" save() method.

    def __unicode__(self):
        return '%s' % self.file

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

class CodeTestInstructionsJSON(models.Model):
    title = models.CharField(max_length=50)
    json = JSONField(blank=True, null=True)
    module = models.ForeignKey(Module,blank=True, null=True)
    code_type = models.ForeignKey(CodeType,blank=True, null=True)

    class Meta:
        verbose_name = 'JSON Test with Instructions'
        verbose_name_plural = 'JSON Tests with Instructions'

    def __unicode__(self):
        return self.title

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
    date = models.DateTimeField(default=timezone.now)

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

class Setting(models.Model):
    name = models.CharField(max_length=50, unique=True)
    value = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name
