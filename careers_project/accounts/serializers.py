from django.contrib.auth import get_user_model
from rest_framework.serializers import Serializer, ModelSerializer, CharField, EmailField, ValidationError

User = get_user_model()


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class UserPasswordSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name',
                  'email', 'password']
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }


class LoginSerializer(Serializer):
    email = EmailField()
    password = CharField()
    
    def validate(self, data):
        if not User.objects.filter(email=data['email']).exists():
            raise ValidationError('Account Not Found')
        return data


class ForgetPasswordSerializer(Serializer):
    email = EmailField()
        
    def validate(self, data):
        if not User.objects.filter(email=data['email']).exists():
            raise ValidationError('User not registered with this email address')
        return data


class ResetPasswordSerializer(Serializer):
    password = CharField()
