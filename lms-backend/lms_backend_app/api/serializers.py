from django.contrib.auth.models import User, Group
from rest_framework import serializers
from lms_backend_app.models import UserProfile, Course, CustomContentType, FeedbackType, CodeType, Question, Note, \
    Feedback, Module, BinaryContent, TextContent, Test, UnitTest, Choice, TestResult, Tag, Attendance, Code, Setting, \
    CodeTestInstructionsJSON, AccessLog, Attendance, DailyScoresTech, DailyScoresSocial, DailyScoresParticipation
from lmsbackend import settings
import os
import json
import urlparse
from datetime import datetime, timedelta, time

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group

class UserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True)
    course = serializers.SerializerMethodField()
    course_id = serializers.SerializerMethodField()
    inmate_id = serializers.SerializerMethodField()
    profile_image = serializers.SerializerMethodField()
    attendance = serializers.SerializerMethodField()
    attendance_id = serializers.SerializerMethodField()
    tech_score = serializers.SerializerMethodField()
    tech_score_id = serializers.SerializerMethodField()
    social_score = serializers.SerializerMethodField()
    social_score_id = serializers.SerializerMethodField()
    participation_score = serializers.SerializerMethodField()
    participation_score_id = serializers.SerializerMethodField()

    def get_course(self, obj):
        profile, created = UserProfile.objects.get_or_create(user=obj)
        if profile.course != None:
            return profile.course.name
        return None

    def get_course_id(self, obj):
        profile, created = UserProfile.objects.get_or_create(user=obj)
        if profile.course != None:
            return profile.course.id
        return None

    def get_inmate_id(self,obj):
        profile, created = UserProfile.objects.get_or_create(user=obj)
        return profile.inmate_id

    def get_profile_image(self,obj):
        profile, created = UserProfile.objects.get_or_create(user=obj)
        return profile.profile_image.name

    def get_attendance(self,obj):
        today = datetime.now().date()
        tomorrow = today + timedelta(1)
        today_start = datetime.combine(today, time())
        today_end = datetime.combine(tomorrow, time())
        record, created = Attendance.objects.get_or_create(student=obj, date__lte=today_end, date__gte=today_start)
        if created:
            record.attendance = True
        return record.attendance

    def get_attendance_id(self,obj):
        today = datetime.now().date()
        tomorrow = today + timedelta(1)
        today_start = datetime.combine(today, time())
        today_end = datetime.combine(tomorrow, time())
        record, created = Attendance.objects.get_or_create(student=obj, date__lte=today_end, date__gte=today_start)
        if created:
            record.attendance = True
        return record.id

    def get_tech_score(self,obj):
        today = datetime.now().date()
        tomorrow = today + timedelta(1)
        today_start = datetime.combine(today, time())
        today_end = datetime.combine(tomorrow, time())
        record, created = DailyScoresTech.objects.get_or_create(student=obj, date__lte=today_end, date__gte=today_start)
        return record.score

    def get_tech_score_id(self,obj):
        today = datetime.now().date()
        tomorrow = today + timedelta(1)
        today_start = datetime.combine(today, time())
        today_end = datetime.combine(tomorrow, time())
        record, created = DailyScoresTech.objects.get_or_create(student=obj, date__lte=today_end, date__gte=today_start)
        return record.id

    def get_social_score(self,obj):
        today = datetime.now().date()
        tomorrow = today + timedelta(1)
        today_start = datetime.combine(today, time())
        today_end = datetime.combine(tomorrow, time())
        record, created = DailyScoresSocial.objects.get_or_create(student=obj, date__lte=today_end, date__gte=today_start)
        return record.score

    def get_social_score_id(self,obj):
        today = datetime.now().date()
        tomorrow = today + timedelta(1)
        today_start = datetime.combine(today, time())
        today_end = datetime.combine(tomorrow, time())
        record, created = DailyScoresSocial.objects.get_or_create(student=obj, date__lte=today_end, date__gte=today_start)
        return record.id

    def get_participation_score(self,obj):
        today = datetime.now().date()
        tomorrow = today + timedelta(1)
        today_start = datetime.combine(today, time())
        today_end = datetime.combine(tomorrow, time())
        record, created = DailyScoresParticipation.objects.get_or_create(student=obj, date__lte=today_end, date__gte=today_start)
        return record.score

    def get_participation_score_id(self,obj):
        today = datetime.now().date()
        tomorrow = today + timedelta(1)
        today_start = datetime.combine(today, time())
        today_end = datetime.combine(tomorrow, time())
        record, created = DailyScoresParticipation.objects.get_or_create(student=obj, date__lte=today_end, date__gte=today_start)
        return record.id

    class Meta:
        model = User

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance

class DailyScoresTechSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyScoresTech

class DailyScoresSocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyScoresSocial

class DailyScoresParticipationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyScoresParticipation

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
    file_url = serializers.SerializerMethodField()
    directory_contents = serializers.SerializerMethodField()
    relative_url = serializers.SerializerMethodField()

    def get_file_url(self, obj):
        return urlparse.urljoin(obj.file.url, urlparse.urlparse(obj.file.url).path)

    def get_relative_url(self, obj):
        return urlparse.urlparse(obj.file.url).path

    def get_directory_contents(self, obj):
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
        fields = ('id', 'name', 'description','file','index_file', 'index_file_list', 'file_url','thumbnail','is_global','content_type', 'extracted_path')

class BinaryContentSerializerUltraLite(serializers.ModelSerializer):
    file_url = serializers.SerializerMethodField('get_url')

    def get_url(self, obj):
        return obj.file.url

    class Meta:
        model = BinaryContent
        fields = ('id', 'name', 'description','index_file','index_file_list','file_url','thumbnail','is_global','content_type', 'extracted_path')


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

class CodeTestInstructionsJSONSerializer(serializers.ModelSerializer):
    json = serializers.SerializerMethodField('get_json_clean')

    def get_json_clean(self, obj):
        return json.loads(json.dumps(obj.json))

    class Meta:
        model = CodeTestInstructionsJSON

class AccessLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessLog

