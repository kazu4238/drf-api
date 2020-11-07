
from django.urls import path
from django.conf.urls import include
# views.pyでModelViewSetを継承している場合にはroutersを用いることができる
from rest_framework import routers
from api.views import TaskViewSet,UserViewSet,ManageUserView

routers = routers.DefaultRouter()
routers.register('tasks',TaskViewSet)
routers.register('users',UserViewSet)

urlpatterns = [
    # views.pyでgenericsを継承している場合には、通常通り.as_view()で表記する
    path('myself/',ManageUserView.as_view(),name='myself'),
    path('',include(routers.urls)),


]
