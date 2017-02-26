import time

from rest_framework import viewsets

from resume.apps.pages.models import Page
from .serializers import PageSerializer


class PageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    lookup_field = 'slug'

    def retrieve(self, request, *args, **kwargs):
        if 'sleep' in request.GET:
            time.sleep(int(request.GET['sleep']))
        return super(PageViewSet, self).retrieve(request, *args, **kwargs)
