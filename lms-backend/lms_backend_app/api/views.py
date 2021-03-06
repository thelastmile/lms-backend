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
from rest_framework.decorators import api_view
from django.db.models import Q
from lmsbackend import settings
import os

@api_view()
def list_system_vars(request):
    """
    View to list local system info

    * Requires token authentication.
    * Only super admin users are able to access this view.
    """
    #authentication_classes = (authentication.TokenAuthentication,)
    #permission_classes = (permissions.IsAdminUser,)

    """
    Find out where we are
    """
    current_script_file_path = os.path.abspath(__file__)
    current_script_directory_path = os.path.dirname(os.path.abspath(__file__))
    current_working_directory = os.getcwd()
    tmp_directory_listing = os.listdir(settings.FILE_UPLOAD_TEMP_DIR)
    

    data = {"current_script_file_path":current_script_file_path,
        "current_script_directory_path":current_script_directory_path,
        "current_working_directory":current_working_directory,
        "tmp_directory_listing":tmp_directory_listing}
    return Response(data)

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
        self.get_or_create_user_profile(user)
        return Response({'token': token.key, 'user': user_serializer.data})

    def get_or_create_user_profile(self, user):
        profile = None
        try:
            profile = UserProfile.objects.get(user=user)
        except UserProfile.DoesNotExist:
            profile = UserProfile.objects.create(user=user)
        return profile


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
        return queryset

class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned set to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = User.objects.filter(Q(groups__name='Student') | Q(groups__name='Inmate'))
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(username=username)
        return queryset

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

class DailyScoresTechViewSet(viewsets.ModelViewSet):
    queryset = DailyScoresTech.objects.all()
    serializer_class = DailyScoresTechSerializer

class DailyScoresSocialViewSet(viewsets.ModelViewSet):
    queryset = DailyScoresSocial.objects.all()
    serializer_class = DailyScoresSocialSerializer

class DailyScoresParticipationViewSet(viewsets.ModelViewSet):
    queryset = DailyScoresParticipation.objects.all()
    serializer_class = DailyScoresParticipationSerializer

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

class AttendanceGraphViewDaily(APIView):
    renderer_classes = (JSONRenderer, )
    def get(self, request, format=None):
        main_object = dict()
        today = datetime.now().date()
        tomorrow = today + timedelta(1)
        today_start = datetime.combine(today, time(hour=0, minute=0, second=0))
        today_end = datetime.combine(tomorrow, time())
        queryset = Attendance.objects.filter(date__gte=today_start,student__groups__name='Student').only('student','date','attendance')

        super_master = dict()
        data_object_master = list()
        for s in queryset:
            data_object = list()
            if s.attendance == True:
                val = 100
            else:
                val = 0
            data_object.append("%s %s" % (s.student.first_name,s.student.last_name))
            data_object.append(val)
            data_object_master.append(data_object)

        main_object = {"label": "In Attendance","color": "#2E90B3"}
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
            data_object.append("%s %s" % (s.student.first_name,s.student.last_name))
            data_object.append(val)
            data_object_master.append(data_object)

        main_object = {"label": "","color": "#2E90B3"}
        #main_object = {"label": "Half Attendance","color": "#2E90B3"}
        main_object.update({"data":data_object_master})

        super_master2.update(main_object)
        
        super_master3 = dict()
        data_object_master = list()
        for s in queryset:
            data_object = list()
            if s.attendance == None:
                val = 5
            else:
                val = 0
            data_object.append("%s %s" % (s.student.first_name,s.student.last_name))
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

class CodeViewSet(viewsets.ModelViewSet):
    queryset = Code.objects.all()
    serializer_class = CodeSerializer

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
    queryset = Note.objects.order_by('-id').all()
    serializer_class = NoteSerializer

    def get_queryset(self):
        print self.request.user
        if self.request.user.is_staff or self.request.user.groups.filter(name="Faculty").exists():
            # Filter by student - TEACHERS ONLY
            student = self.request.query_params.get('student', None)
            queryset = Note.objects.order_by('-id').all()
            if student is not None:
                queryset = queryset.filter(author__id=student)
        else:
            queryset = Note.objects.order_by('-id').filter(instructor_author__isnull=True).filter(author=self.request.user)
        return queryset

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.order_by('order').all()
    serializer_class = ModuleSerializer

    def get_queryset(self):
        queryset = Module.objects.order_by('order').all()
        course = self.request.query_params.get('course', None)
        if course is not None:
            queryset = queryset.filter(course__id=course)
        return queryset

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
        queryset = BinaryContent.objects.order_by('order').all()
        module = self.request.query_params.get('module', None)
        if module is not None and module != "undefined":
            queryset = queryset.filter(module__id=module)

        content_type = self.request.query_params.get('content_type', None)
        if content_type == '5' or content_type == 'resources':
            queryset = BinaryContent.objects.filter((Q(is_global=True) | Q(content_type__name__icontains="Asset") | Q(content_type__name__icontains="Image") | Q(content_type__name__icontains="Docs"))).order_by('content_type')
            print queryset
            print content_type
            print "HERE"
        elif content_type is not None:
            # Strip an ending S if it has one
            if content_type[-1] == "s":
                content_type = content_type[:-1]

            queryset = queryset.filter(content_type__name__icontains=content_type)
            print "here"
        
        return queryset

class BinaryContentViewSetUltraLite(viewsets.ModelViewSet):
    serializer_class = BinaryContentSerializerUltraLite

    def get_queryset(self):
        """
        Optionally restricts the returned set to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = BinaryContent.objects.order_by('order').all()
        module = self.request.query_params.get('module', None)
        if module is not None:
            queryset = queryset.filter(module__id=module)

        content_type = self.request.query_params.get('content_type', None)
        if content_type is not None and content_type != '5':
            queryset = queryset.filter(content_type__id=content_type)
        elif content_type == '5':
            queryset = BinaryContent.objects.filter(is_global=True).order_by('content_type')
            print content_type
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


class CodeRunResultViewSet(viewsets.ModelViewSet):
    queryset = CodeRunResult.objects.all()
    serializer_class = CodeRunResultSerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class SettingViewSet(viewsets.ModelViewSet):
    serializer_class = SettingSerializer
    # create defaults
    Setting.objects.get_or_create(name="HomeContent")
    queryset = Setting.objects.all()

    def get_queryset(self):
        queryset = Setting.objects.all()
        setting_name = self.request.query_params.get('name', None)
        if setting_name is not None:
            queryset = queryset.filter(name=setting_name)
        return queryset

class CodeTestInstructionsJSONViewSet(viewsets.ModelViewSet):
    queryset = CodeTestInstructionsJSON.objects.all()
    serializer_class = CodeTestInstructionsJSONSerializer

class AccessLogViewSet(viewsets.ModelViewSet):
    queryset = AccessLog.objects.all()
    serializer_class = AccessLogSerializer

    def get_queryset(self):
        queryset = AccessLog.objects.all()
        userid = self.request.query_params.get('user', None)
        if userid is not None and userid != "":
            queryset = queryset.filter(user__id=userid.strip("/")).order_by('-id')[:1]
        return queryset

class HomePageContentViewSet(viewsets.ModelViewSet):
    queryset = HomePageContent.objects.all()
    serializer_class = HomePageContentSerializer

    def get_queryset(self):
        queryset = HomePageContent.objects.all()
        course = self.request.query_params.get('course', None)
        if course is not None:
            course_obj = Course.objects.filter(id=course)
            if len(course_obj) >= 1:
                queryset, created = HomePageContent.objects.get_or_create(course=course_obj[0])
            queryset = HomePageContent.objects.filter(course__id=course)
        return queryset
