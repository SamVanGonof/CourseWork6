from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['role'] = serializers.CharField(max_length=5, write_only=True, required=False)


class CurrentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'image']
