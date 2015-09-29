from django.contrib.auth.models import User, Group
from rest_framework import serializers
from CrazyNumbersApp.models import UserProfile

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		# Un - comment below for the optional object model attributes
		fields = ('user', 'course', 'inmate_id', )