from rest_framework import serializers

from .models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')

class UserGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('groups')

