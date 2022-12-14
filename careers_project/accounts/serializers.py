from django.contrib.auth.models import User

from rest_framework.serializers import Serializer, ModelSerializer


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']


class UserPasswordSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name',
                  'email', 'username', 'password']
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }


class LoginSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "password"]

