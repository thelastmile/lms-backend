from django.conf.urls import include, url
from django.contrib import admin
from lms_backend_app import urls as lms_backend_app_urls

urlpatterns = [
    # Examples:
    # url(r'^$', 'lmsbackend.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include(lms_backend_app_urls))
]
