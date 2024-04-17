from rest_framework import serializers

from .models import Task, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']


class TaskSerializer(serializers.ModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        queryset=User.objects.all(),
        view_name='get_all_users'
    )

    class Meta:
        model = Task
        fields = ['title', 'user']
