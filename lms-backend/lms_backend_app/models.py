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
import boto
from boto.s3.key import Key
import shutil
import json

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
    instructor = models.ForeignKey(User, related_name='instructor',blank=True, null=True)
    attendance = models.NullBooleanField(choices = ATTENDANCE_CHOICES)
    date = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return '%s %s %s' % (self.student, self.date, self.attendance)


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
    content_type = models.ForeignKey(ContentType,blank=True, null=True)
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    date = models.DateTimeField(default=timezone.now)
    instructor_author = models.ForeignKey(User,blank=True, null=True, related_name='note_instructor_author')

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
    index_file_list = JSONField(blank=True, null=True) # Temp field for storing selections of options as to the main index file for archives

    def uploadResultToS3(self, awsid,awskey,bucket,source_folder,to_path,uuid): 
        c = boto.connect_s3(awsid,awskey) 
        b = c.get_bucket(bucket) 
        k = Key(b)
        index_file_list = []
        for path,directory,files in os.walk(source_folder):
            destination_file_path = path.split('/',1)[1]
            for file in files:
                destination_path = os.path.relpath(os.path.join(to_path,destination_file_path,file))
                relpath = os.path.relpath(os.path.join(path,file))
                if 'index.htm' in file:
                    index_file_list.append(os.path.relpath(os.path.join(destination_file_path,file).split('/',1)[1]));
                if not b.get_key(relpath):
                    print 'sending  ...%s' % relpath[-30:]
                    k.key = destination_path
                    k.set_contents_from_filename(relpath)
                    try:
                        k.set_acl('public-read')
                    except:
                        print "failed"
        prefix = os.path.join(to_path,uuid)
        rs = b.get_all_keys(prefix=prefix)
        print rs
        for r in rs:
            print r.key
        return json.dumps(index_file_list)

    def save(self, *args, **kwargs):
        if self.pk is None:
            """
            Unzip on local temp area, upload to S3 or another connector
            """
            ext = self.file.name.split(".")[-1].lower()
            directoryname = '%s' % (uuid.uuid4())
            if ext.lower() == 'zip':
                zfile = zipfile.ZipFile(self.file)
                self.extracted_path = '%s/%s/' % (settings.FILE_UPLOAD_TEMP_DIR, directoryname)
                zfile.extractall(self.extracted_path)

            if settings.COPY_UPLOADED_FILES_TO_S3:
                self.index_file_list = self.uploadResultToS3(settings.AWS_ACCESS_KEY_ID,
                    settings.AWS_SECRET_ACCESS_KEY,
                    settings.AWS_STORAGE_BUCKET_NAME,
                    self.extracted_path,
                    settings.MEDIA_HTML,
                    directoryname)
                """
                Now DELETE the temp path
                and reset the path to that on S3
                """
                shutil.rmtree(self.extracted_path, ignore_errors=True)
                self.extracted_path = "/%s%s/" % (settings.MEDIA_HTML,directoryname)


        super(BinaryContent, self).save(*args, **kwargs)

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

class AccessLog(models.Model):
    user = models.ForeignKey(User)
    path = models.TextField(blank=True, null=True)
    created = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return "%s %s %s" % (self.user, self.created, self.path)

class DailyScoresTech(models.Model):
    student = models.ForeignKey(User, related_name='student_tech')
    instructor = models.ForeignKey(User, related_name='instructor_tech',blank=True, null=True)
    score = models.PositiveIntegerField(blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return "%s %s %s" % (self.student, self.date, self.score)

class DailyScoresSocial(models.Model):
    student = models.ForeignKey(User, related_name='student_social')
    instructor = models.ForeignKey(User, related_name='instructor_social',blank=True, null=True)
    score = models.PositiveIntegerField(blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return "%s %s %s" % (self.student, self.date, self.score)

class DailyScoresParticipation(models.Model):
    student = models.ForeignKey(User, related_name='_participation')
    instructor = models.ForeignKey(User, related_name='instructor_participation',blank=True, null=True)
    score = models.PositiveIntegerField(blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return "%s %s %s" % (self.student, self.date, self.score)