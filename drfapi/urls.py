
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('api.urls')),
    # obtain_auth_tokenとはdjango rest frameworkで用意されている、
    # ユーザネームとパスワードをPOSTするとそのユーザのTokenが返ってくる関数である
    path('auth/',obtain_auth_token),
]
