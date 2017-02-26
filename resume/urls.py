"""resume URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view

from resume.apps.pages.api.views import PageViewSet
from resume.apps.resumes.api.views import ResumeViewSet
from resume.apps.users.api.views import UserViewSet

schema_view = get_swagger_view(title='Resume API')


router = DefaultRouter()
router.register(r'pages', PageViewSet)
router.register(r'resumes', ResumeViewSet)
router.register(r'users', UserViewSet)


urlpatterns = [
    url(r'^$', schema_view),
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
]
