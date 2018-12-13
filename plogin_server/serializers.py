import rest_auth.serializers
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from plogin_server.models import Team
from plogin_server.models import Contest, Session


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'id', 'first_name',
                  'last_name', 'email', 'date_joined')


class UserOuterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class TeamOuterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('id', 'name')


class ContestOuterSerializer(serializers.ModelSerializer):
    winner = TeamOuterSerializer(read_only=True)

    class Meta:
        model = Contest
        fields = ('id', 'name', 'start_timestamp', 'end_timestamp', 'winner')


class TeamSerializer(serializers.ModelSerializer):
    captain = UserOuterSerializer(read_only=True)
    members = UserOuterSerializer(read_only=True, many=True)
    contests = ContestOuterSerializer(read_only=True, many=True)

    class Meta:
        model = Team
        fields = ('id', 'name', 'captain', 'members', 'contests')


class TeamCreateSerializer(serializers.ModelSerializer):
    captain = serializers.ReadOnlyField(source='captain.id')
    members = serializers.PrimaryKeyRelatedField(read_only=False,
                                                 many=True,
                                                 queryset=User.objects.all())

    class Meta:
        model = Team
        fields = ('id', 'name', 'captain', 'members')


class ContestSerializer(serializers.ModelSerializer):
    winner = TeamOuterSerializer(read_only=True)
    teams = TeamOuterSerializer(read_only=True, many=True)

    class Meta:
        model = Contest
        fields = ('id', 'name', 'start_timestamp',
                  'end_timestamp', 'teams', 'winner',
                  'team_max_size', 'sport_type')


class ContestCreateSerializer(serializers.ModelSerializer):
    teams = serializers.PrimaryKeyRelatedField(read_only=False,
                                               many=True,
                                               queryset=Team.objects.all())

    class Meta:
        model = Contest
        fields = ('id', 'name', 'teams', 'team_max_size',
                  'start_timestamp', 'end_timestamp')


class SessionSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    contest = serializers.ReadOnlyField(source='contest.id')

    class Meta:
        model = Session
        fields = ('user', 'contest', 'collected')
