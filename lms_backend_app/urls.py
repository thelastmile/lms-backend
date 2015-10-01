from django.conf.urls import url, include
from . import views
from .api.views import *
from rest_framework import routers

# API router set up
router = routers.DefaultRouter()
router.register(r'users', UserViewSet, base_name='users')
router.register(r'course', CourseViewSet, base_name='course')
router.register(r'attendance', AttendanceViewSet, base_name='attendance')
router.register(r'customcontenttype', CustomContentTypeViewSet, base_name='customcontenttype')
router.register(r'feedbacktype', FeedbackTypeViewSet, base_name='feedbacktype')
router.register(r'codetype', CodeTypeViewSet, base_name='codetype')
router.register(r'question', QuestionViewSet, base_name='question')
router.register(r'note', NoteViewSet, base_name='note')
router.register(r'feedback', FeedbackViewSet, base_name='feedback')
router.register(r'module', ModuleViewSet, base_name='module')
router.register(r'binarycontent', BinaryContentViewSet, base_name='binarycontent')
router.register(r'textcontent', TextContentViewSet, base_name='textcontent')
router.register(r'test', TestResultViewSet, base_name='test')
router.register(r'unittest', UnitTestViewSet, base_name='unittest')
router.register(r'choice', ChoiceViewSet, base_name='choice')
router.register(r'testresult', TestResultViewSet, base_name='testresult')
router.register(r'tag', TagViewSet, base_name='tag')


# just general index and api setup for now
urlpatterns = [
	url(r'^api/', include(router.urls)),
	url(r'^$', views.index, name='index'),
]
