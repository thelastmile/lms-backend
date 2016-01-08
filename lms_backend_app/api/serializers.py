from django.contrib.auth.models import User, Group
from rest_framework import serializers
from lms_backend_app.models import UserProfile, Course, CustomContentType, FeedbackType, CodeType, Question, Note, \
    Feedback, Module, BinaryContent, TextContent, Test, UnitTest, Choice, TestResult, Tag, Attendance, Code, Setting
from lmsbackend import settings
import os

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group

class UserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True)
    course = serializers.SerializerMethodField()
    inmate_id = serializers.SerializerMethodField()
    profile_image = serializers.SerializerMethodField()

    def get_course(self, obj):
        profile, created = UserProfile.objects.get_or_create(user=obj)
        if profile.course != None:
            return profile.course.name
        return None

    def get_inmate_id(self,obj):
        profile, created = UserProfile.objects.get_or_create(user=obj)
        return profile.inmate_id

    def get_profile_image(self,obj):
        profile, created = UserProfile.objects.get_or_create(user=obj)
        return profile.profile_image.name

    class Meta:
        model = User

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course

class CustomContentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomContentType

class FeedbackTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackType

class CodeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodeType

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module

class CodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Code

class BinaryContentSerializer(serializers.ModelSerializer):
    file_url = serializers.SerializerMethodField('get_url')
    directory_contents = serializers.SerializerMethodField('get_dir_structure')

    def get_url(self, obj):
        return obj.file.url

    def get_dir_structure(self, obj):
        path = '%s%s' % (settings.MEDIA_ROOT,obj.extracted_path)
        if path:
            extracted_path_html = ''
            for path, dirs, files in os.walk(path):
              extracted_path_html = '<div class="files-dir">%s</div>%s' % (path,extracted_path_html)
              for f in files:
                api_file_path = '%s%s/%s' % (settings.MEDIA_URL,path.replace(settings.MEDIA_ROOT,''),f)
                extracted_path_html = '<a class="files-file" ng-click="ALC.LFILEindexPath=\'%s\';ALC.LFILEselectIndexPath()">%s</a>%s' % (api_file_path,f,extracted_path_html)
            return extracted_path_html
        else:
            return '<div>Directory appears empty or incorrect.</div>'

    class Meta:
        model = BinaryContent

class BinaryContentSerializerLite(serializers.ModelSerializer):
    file_url = serializers.SerializerMethodField('get_url')

    def get_url(self, obj):
        return obj.file.url

    class Meta:
        model = BinaryContent
        fields = ('id', 'name', 'description','file','index_file','file_url','thumbnail','is_global','content_type')

class TextContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextContent

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test

class UnitTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitTest

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice

class TestResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestResult

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag

class SettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setting
