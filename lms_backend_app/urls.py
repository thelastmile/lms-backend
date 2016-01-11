from django.conf.urls import url, include
from . import views
from .api.views import *
from rest_framework import routers
from django.conf.urls.static import static

# API router set up
router = routers.DefaultRouter()
router.register(r'users', UserViewSet, base_name='users')
router.register(r'students', StudentViewSet, base_name='students')
router.register(r'course', CourseViewSet, base_name='course')
router.register(r'attendance', AttendanceViewSet, base_name='attendance')
router.register(r'customcontenttype', CustomContentTypeViewSet, base_name='customcontenttype')
router.register(r'feedbacktype', FeedbackTypeViewSet, base_name='feedbacktype')
router.register(r'codetype', CodeTypeViewSet, base_name='codetype')
router.register(r'code', CodeViewSet, base_name='code')
router.register(r'question', QuestionViewSet, base_name='question')
router.register(r'note', NoteViewSet, base_name='note')
router.register(r'feedback', FeedbackViewSet, base_name='feedback')
router.register(r'module', ModuleViewSet, base_name='module')
router.register(r'binarycontent', BinaryContentViewSet, base_name='binarycontent')
router.register(r'binarycontentlite', BinaryContentViewSetLite, base_name='binarycontentlite')
router.register(r'binarycontentultralite', BinaryContentViewSetUltraLite, base_name='binarycontentlite')
router.register(r'textcontent', TextContentViewSet, base_name='textcontent')
router.register(r'test', TestResultViewSet, base_name='test')
router.register(r'unittest', UnitTestViewSet, base_name='unittest')
router.register(r'choice', ChoiceViewSet, base_name='choice')
router.register(r'testresult', TestResultViewSet, base_name='testresult')
router.register(r'tag', TagViewSet, base_name='tag')
router.register(r'setting', SettingViewSet, base_name='setting')
router.register(r'jsoncode', CodeTestInstructionsJSONViewSet, base_name='setting')


# just general index and api setup for now
urlpatterns = [
	url(r'^api/docs/', include('rest_framework_swagger.urls')),
	url(r'^api/', include(router.urls)),
	url(r'^$', views.index, name='index'),
	url(r'^api/attendancegraphdaily/$', AttendanceGraphViewDaily.as_view()),
	#url(r'^api/binarycontent/$', BinaryContentView.as_view()),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
