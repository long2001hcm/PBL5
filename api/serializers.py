from dataclasses import field
from rest_framework import serializers
from .models import User, Notify

class NotifySerializer(serializers.ModelSerializer):
    class Meta:
        model = Notify
        fields = ['idNotify', 'Time', 'Text']
class UserSerializer(serializers.ModelSerializer):
    notify = NotifySerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ['idUser', 'Name', 'notify']
