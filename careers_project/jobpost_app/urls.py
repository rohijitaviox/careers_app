from django.urls import path
from .api import JobsViewset

app_name = "jobpost_app"

urlpatterns = [
    path("search/<str:title>", JobsViewset.as_view({"get":"search"}), name="search")
]
