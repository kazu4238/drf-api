from django.shortcuts import render

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from django.contrib.auth.models import User
from .models import Task
from rest_framework import viewsets
from .serializers import TaskSerializer, UserSerializer
from .ownpermissions import ProfilePermission


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # 誰でもアクセスしてCRUDできるようにする時はAllowAny、
    # ownpermissions.pyで作成したProfilePermissionを適用する
    permission_classes = (ProfilePermission,)


# myselfのエンドポイント
class ManageUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    # ログインしているユーザのみ許可
    authentication_classes = TokenAuthentication,
    permission_classes = IsAuthenticated,

    # ログインしているユーザの情報を返す
    def get_object(self):
        return self.request.user


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    # ログインしているユーザのみ許可
    authentication_classes = TokenAuthentication,
    permission_classes = (IsAuthenticated,)
