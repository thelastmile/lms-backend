from django.conf.urls import url, include
from . import views
from .api.views import UserViewSet
from rest_framework import routers

# API router set up
router = routers.DefaultRouter()
router.register(r'users', UserViewSet, base_name='users')

# just general index and api setup for now
urlpatterns = [
	url(r'^api/', include(router.urls)),
	url(r'^$', views.index, name='index'),
]
