from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from .serializers import *
from lms_backend_app.models import *
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from rest_framework import parsers, renderers
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime, timedelta, time
from django.core import serializers
import json
from rest_framework.decorators import detail_route

class ObtainAuthToken(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        user_serializer = UserSerializer(user)
        return Response({'token': token.key, 'user': user_serializer.data})


obtain_auth_token = ObtainAuthToken.as_view()

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned set to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = User.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(username=username)
            #user = queryset.get()
            #print user.groups
            #user.groups = [user.groups.all()]
        return queryset

class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned set to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = User.objects.filter(groups__name='Inmate')
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(username=username)
        return queryset

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

class AttendanceGraphViewDaily(APIView):
    renderer_classes = (JSONRenderer, )
    def get(self, request, format=None):
        main_object = dict()
        today = datetime.now().date()
        tomorrow = today + timedelta(1)
        today_start = datetime.combine(today, time())
        today_end = datetime.combine(tomorrow, time())
        queryset = Attendance.objects.filter(date__gte=today_start,student__groups__name='Inmate').only('student','date','attendance')

        super_master = dict()
        data_object_master = list()
        for s in queryset:
            data_object = list()
            if s.attendance == True or s.attendance == False:
                val = 100
            else:
                val = 0
            data_object.append(s.student.username)
            data_object.append(val)
            data_object_master.append(data_object)

        main_object = {"label": "Full Attendance","color": "green"}
        main_object.update({"data":data_object_master})
        super_master.update(main_object)

        super_master2 = dict()
        data_object_master = list()
        for s in queryset:
            data_object = list()
            if s.attendance == False:
                val = 50
            else:
                val = 0
            data_object.append(s.student.username)
            data_object.append(val)
            data_object_master.append(data_object)

        main_object = {"label": "Half Attendance","color": "yellow"}
        main_object.update({"data":data_object_master})

        super_master2.update(main_object)
        
        super_master3 = dict()
        data_object_master = list()
        for s in queryset:
            data_object = list()
            if s.attendance == None:
                val = 100
            else:
                val = 0
            data_object.append(s.student.username)
            data_object.append(val)
            data_object_master.append(data_object)

        main_object = {"label": "Absent","color": "red"}
        main_object.update({"data":data_object_master})

        super_master3.update(main_object)

        god_set = []
        god_set.append(super_master)
        god_set.append(super_master2)
        god_set.append(super_master3)
        data = json.dumps(god_set)
        return HttpResponse(data, content_type="application/json")

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CustomContentTypeViewSet(viewsets.ModelViewSet):
    queryset = CustomContentType.objects.all()
    serializer_class = CustomContentTypeSerializer

class FeedbackTypeViewSet(viewsets.ModelViewSet):
    queryset = FeedbackType.objects.all()
    serializer_class = FeedbackTypeSerializer

class CodeTypeViewSet(viewsets.ModelViewSet):
    queryset = CodeType.objects.all()
    serializer_class = CodeTypeSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer

class BinaryContentViewSet(viewsets.ModelViewSet):
    serializer_class = BinaryContentSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned set to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = BinaryContent.objects.all()
        module = self.request.query_params.get('module', None)
        if module is not None:
            queryset = queryset.filter(module__id=module)

        content_type = self.request.query_params.get('content_type', None)
        if content_type is not None:
            queryset = queryset.filter(content_type__id=content_type)
        return queryset

class BinaryContentViewSetLite(viewsets.ModelViewSet):
    serializer_class = BinaryContentSerializerLite

    def get_queryset(self):
        """
        Optionally restricts the returned set to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = BinaryContent.objects.all()
        module = self.request.query_params.get('module', None)
        if module is not None:
            queryset = queryset.filter(module__id=module)

        content_type = self.request.query_params.get('content_type', None)
        if content_type is not None:
            queryset = queryset.filter(content_type__id=content_type)
        return queryset

class TextContentViewSet(viewsets.ModelViewSet):
    queryset = TextContent.objects.all()
    serializer_class = TextContentSerializer

class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

class UnitTestViewSet(viewsets.ModelViewSet):
    queryset = UnitTest.objects.all()
    serializer_class = UnitTestSerializer

class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

class TestResultViewSet(viewsets.ModelViewSet):
    queryset = TestResult.objects.all()
    serializer_class = TestResultSerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
