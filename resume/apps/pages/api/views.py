import time

from rest_framework import viewsets
from rest_framework.exceptions import APIException
from rest_framework.permissions import AllowAny

from resume.apps.pages.models import Page
from .serializers import PageSerializer


class PageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    lookup_field = 'slug'
    # permission_classes = (AllowAny,)

    def retrieve(self, request, *args, **kwargs):
        if 'sleep' in request.GET:
            time.sleep(int(request.GET['sleep']))
        if 'error' in request.GET:
            raise APIException()
        return super(PageViewSet, self).retrieve(request, *args, **kwargs)
