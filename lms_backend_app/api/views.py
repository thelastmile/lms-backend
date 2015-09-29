from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer
from lms_backend_app.models import UserProfile


class UserViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer
