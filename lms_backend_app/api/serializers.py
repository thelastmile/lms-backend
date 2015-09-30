from django.contrib.auth.models import User, Group
from rest_framework import serializers
from lms_backend_app.models import UserProfile

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserProfile
		# Un - comment below for the optional object model attributes
		fields = ('user', 'course', 'inmate_id', )

	# TODO SERIALIZE ALL MODELS.