from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Course)
admin.site.register(Question)
admin.site.register(Tag)
admin.site.register(Module)
admin.site.register(CodeType)