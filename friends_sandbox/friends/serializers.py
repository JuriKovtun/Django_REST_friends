from django.contrib.auth.models import User, Group
from rest_framework import serializers
from friendship.models import FriendshipRequest


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class FriendshipRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendshipRequest
        fields = ['id', 'from_user', 'to_user',
                  'message', 'created', 'rejected', 'viewed']
