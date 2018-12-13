"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth.models import User, Group
from django.contrib import admin
from rest_framework import permissions, routers, serializers, viewsets
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope,\
    TokenHasScope
from plogin_server import views

admin.autodiscover()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['groups']
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^user-teams/', views.UsersTeamList.as_view()),
    url(r'^user-contests/', views.UserContestList.as_view()),
    url(r'^create-team/', views.UserCreateTeam.as_view()),
    url(r'^team/(?P<pk>[0-9]+)$', views.TeamDetail.as_view()),
    url(r'^contest/(?P<pk>[0-9]+)$', views.ContestDetail.as_view()),
    url(r'^users-list/', views.UserList.as_view()),
    url(r'^teams-list/', views.TeamsList.as_view()),
    url(r'^create-contest/', views.UserCreateContest.as_view()),
    url(r'^sessions/$', views.SessionList.as_view()),
    url(r'^sessions/(?P<pk>[0-9]+)/$', views.SessionDetail.as_view()),
]
