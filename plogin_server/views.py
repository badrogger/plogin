from rest_framework import status
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from rest_framework import generics
from plogin_server.serializers import \
    ContestSerializer, ContestOuterSerializer, \
    TeamSerializer, TeamOuterSerializer, \
    UserOuterSerializer, TeamCreateSerializer, \
    ContestCreateSerializer, SessionSerializer

from plogin_server.models import Team, Contest, Session
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response


class TeamDetail(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class ContestDetail(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Contest.objects.all()
    serializer_class = ContestSerializer


class UsersTeamList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return user.team_set.all()

    serializer_class = TeamSerializer


class UserCreateTeam(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        members = self.request.data['members']
        members.append(self.request.user.id)
        serializer.save(captain=self.request.user, members=members)

    serializer_class = TeamCreateSerializer


class UserCreateContest(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        teams = self.request.data['teams']
        serializer.save(teams=teams)

    serializer_class = ContestCreateSerializer


class UserList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return User.objects.all()

    serializer_class = UserOuterSerializer


class UserContestList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        teams = user.team_set.all()
        contests = []
        for team in teams:
            contests.extend(team.contest_set.all())
        return list(set(contests))

    serializer_class = ContestOuterSerializer


class ContestList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Contest.objects.all()
    serializer_class = ContestSerializer


class TeamsList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class SessionList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Session.objects.all()
    serializer_class = SessionSerializer


class SessionDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
