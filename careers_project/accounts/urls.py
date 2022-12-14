from django.urls import path

from .api import UserViewset

app_name = "accounts"

user_views = UserViewset.as_view({
    "get": 'retrieve',
    'post': 'create',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path("login/", UserViewset.as_view({"post": "login"}), name="login"),
    path("logout/", UserViewset.as_view({"get": "logout"}), name="logout"),
    path("list-all/", UserViewset.as_view({"get": "list"}), name="list-all"),
    path("user/", user_views, name="user"),
    # path('forgot-password')
]
