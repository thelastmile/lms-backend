from django.contrib.auth.models import User, Group
from rest_framework import serializers
from lms_backend_app.models import UserProfile, Course, CustomContentType, FeedbackType, CodeType, Question, Note, \
    Feedback, Module, BinaryContent, TextContent, Test, UnitTest, Choice, TestResult, Tag, Attendance

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group

class UserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True)

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


class BinaryContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BinaryContent


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
