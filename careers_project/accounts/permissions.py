from rest_framework.request import Request
from rest_framework.permissions import BasePermission


class UserPermissions(BasePermission):
    def has_permission(self, request: Request, view):
        if view.action == 'list':
            return request.user.is_authenticated and request.user.is_staff
        elif view.action in ("create", "login", "logout",'get_action'):
            return True
        elif view.action in ["retrieve", "update", "partial_update", "destroy"] and request.user.is_authenticated:
            return True
        else:
            return False

    def has_object_permission(self, request: Request, view, obj):
        if not request.user.is_authenticated:
            return False
        if view.action == "retrieve":
            return obj == request.user or request.user.is_superuser
        elif view.action in ["update", "partial_update"]:
            return obj == request.user or request.user.is_superuser
        elif view.action == "destroy":
            return obj == request.user or request.user.is_superuser
        else:
            return False
