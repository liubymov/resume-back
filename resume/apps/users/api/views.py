import time

from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.exceptions import APIException
from rest_framework.permissions import AllowAny

from .permissions import IsStaffOrTargetUser
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects
    serializer_class = UserSerializer
    lookup_field = 'username'
    csrf_exempt = False

    def get_permissions(self):
        return (AllowAny() if self.request.method == 'POST' else IsStaffOrTargetUser()),

    def create(self, request, *args, **kwargs):
        if 'sleep' in request.GET:
            time.sleep(int(request.GET['sleep']))
        if 'error' in request.GET:
            raise APIException()
        return super().create(request, *args, **kwargs)
