from django.urls import path

from .api import UserViewset, ForegetPasswordViewSet
# from rest_framework.routers import DefaultRouter

app_name = "accounts"

user_views = UserViewset.as_view({
    "get": 'retrieve', # get details of authenticated user
    'post': 'create', # create a new user
    'put': 'update', # update existing user
    'patch': 'partial_update', # update existing user
    'delete': 'destroy' # delete user
})

password_change_view = ForegetPasswordViewSet.as_view({
    'post': 'create',
})

urlpatterns = [ 

    path("login/", UserViewset.as_view({"post": "login"}), name="login"),
    path("logout/", UserViewset.as_view({"get": "logout"}), name="logout"),
    path("list-all/", UserViewset.as_view({"get": "list"}), name="list-all"),
    path("user/", user_views, name="user"),
    path("reset_password/<str:token>", ForegetPasswordViewSet.as_view({"post": "reset_password"}), name="reset_password"),
    path("forgetpassword/",ForegetPasswordViewSet.as_view({"post": "create"}), name="forgetpassword"),
    
]
