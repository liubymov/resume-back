from rest_framework import viewsets

from resume.apps.resumes.models import Resume
from .serializers import ResumeSerializer


class ResumeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
