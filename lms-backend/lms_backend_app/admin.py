from django.contrib import admin
from .models import *

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class UserProfileInline(admin.TabularInline):
    model = UserProfile

class MyUserAdmin(UserAdmin):
    inlines = [
        UserProfileInline,
    ]

admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)

admin.site.register(Course)
admin.site.register(Attendance)
admin.site.register(Code)
admin.site.register(CustomContentType)
admin.site.register(FeedbackType)
admin.site.register(CodeType)
admin.site.register(Question)
admin.site.register(Note)
admin.site.register(Feedback)
admin.site.register(Module)
admin.site.register(BinaryContent)
admin.site.register(TextContent)
admin.site.register(Test)
admin.site.register(UnitTest)
admin.site.register(Choice)
admin.site.register(TestResult)
admin.site.register(Tag)
admin.site.register(Setting)
admin.site.register(CodeTestInstructionsJSON)
