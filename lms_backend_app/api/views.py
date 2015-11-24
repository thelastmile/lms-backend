from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.response import Response
from django.http import HttpResponse
from .serializers import *
from lms_backend_app.models import *
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from datetime import datetime, timedelta, time
from django.core import serializers
import json


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


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

class AttendanceGraphViewDaily(APIView):


# '''[{
#   "label": "Serie1",
#   "color": "#FFBE41",
#   "data": [
#     ["Jan", 56],
#     ["Feb", 81],
#     ["Mar", 97],
#     ["Apr", 44],
#     ["May", 24],
#     ["Jun", 85],
#     ["Jul", 94],
#     ["Aug", 78],
#     ["Sep", 52],
#     ["Oct", 17],
#     ["Nov", 90],
#     ["Dec", 62]
#   ]
# }, {
#   "label": "Serie2",
#   "color": "#937fc7",
#   "data": [
#     ["Jan", 69],
#     ["Feb", 135],
#     ["Mar", 14],
#     ["Apr", 100],
#     ["May", 100],
#     ["Jun", 62],
#     ["Jul", 115],
#     ["Aug", 22],
#     ["Sep", 104],
#     ["Oct", 132],
#     ["Nov", 72],
#     ["Dec", 61]
#   ]
# }, {
#   "label": "Serie3",
#   "color": "#00b4ff",
#   "data": [
#     ["Jan", 29],
#     ["Feb", 36],
#     ["Mar", 47],
#     ["Apr", 21],
#     ["May", 5],
#     ["Jun", 49],
#     ["Jul", 37],
#     ["Aug", 44],
#     ["Sep", 28],
#     ["Oct", 9],
#     ["Nov", 12],
#     ["Dec", 35]
#   ]
# }]  '''

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
            print s.student.username
            print s.attendance
            if s.attendance == True or s.attendance == False:
                val = 100
            else:
                val = 0
            data_object.append(s.student.username)
            data_object.append(val)
            data_object_master.append(data_object)
        print data_object_master

        main_object = {"label": "Full Attendance","color": "green"}
        main_object.update({"data":data_object_master})
        super_master.update(main_object)

        super_master2 = dict()
        data_object_master = list()
        for s in queryset:
            data_object = list()
            print s.student.username
            print s.attendance
            if s.attendance == False:
                print "PARTIAL"
                val = 50
            else:
                val = 0
            data_object.append(s.student.username)
            data_object.append(val)
            data_object_master.append(data_object)
        print data_object_master

        main_object = {"label": "Half Attendance","color": "yellow"}
        main_object.update({"data":data_object_master})

        super_master2.update(main_object)
        
        super_master3 = dict()
        data_object_master = list()
        for s in queryset:
            data_object = list()
            print s.student.username
            print s.attendance
            if s.attendance == None:
                val = 100
            else:
                val = 0
            data_object.append(s.student.username)
            data_object.append(val)
            data_object_master.append(data_object)
        print data_object_master

        main_object = {"label": "Absent","color": "red"}
        main_object.update({"data":data_object_master})

        super_master3.update(main_object)

        god_set = []
        god_set.append(super_master)
        god_set.append(super_master2)
        god_set.append(super_master3)
        data = json.dumps(god_set)
        #data = serializers.serialize('json', data_object_master)
        #data = [super_master]
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
    queryset = BinaryContent.objects.all()
    serializer_class = BinaryContentSerializer


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
