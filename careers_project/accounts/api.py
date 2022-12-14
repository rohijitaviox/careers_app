from django.contrib.auth.models import User
from django.db import IntegrityError

from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication

from .serializers import UserSerializer, LoginSerializer, UserPasswordSerializer
from .permissions import UserPermissions


class UserViewset(ModelViewSet):
    queryset = User.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [UserPermissions]

    def get_object(self):
        if self.action in ["list", "create"]:
            return super().get_object()
        elif self.action in ["retrieve", "update", "partial_update", "destroy"]:
            return self.request.user

    def get_serializer_class(self):
        if self.action == "create":
            return UserPasswordSerializer
        elif self.action in ("update", 'partial_update', 'retrieve', 'list'):
            return UserSerializer
        elif self.action in ["login", "destroy"]:
            return LoginSerializer

    def create(self, request: Request, *args, **kwargs):
        serializer = UserPasswordSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = User.objects.create_user(**serializer.validated_data)
            except IntegrityError:
                return Response("Username already exists", status=status.HTTP_400_BAD_REQUEST)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request: Request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user: User = request.user
            if serializer.validated_data['email'] == user.email and \
                    user.check_password(serializer.validated_data['password']):
                user.delete()
                return Response(status=status.HTTP_200_OK)
            else:
                return Response("Invalid credentials", status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def login(self, request: Request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = User.objects.get(
                    email=serializer.validated_data['email'])
            except Exception as e:
                return Response("Email or Password incorrect", status=status.HTTP_401_UNAUTHORIZED)
            if not user.check_password(serializer.validated_data['password']):
                return Response("Email or Password incorrect", status=status.HTTP_401_UNAUTHORIZED)
            # delete old token
            try:
                Token.objects.delete(user=user)
            except:
                pass
            new_token = Token.objects.create(user=user)
            return Response({"token": new_token.key}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def logout(self, request: Request):
        if not self.request.user.is_authenticated:
            return Response(status=status.HTTP_200_OK)
        else:
            Token.objects.filter(user=request.user).delete()
            return Response(status=status.HTTP_200_OK)
