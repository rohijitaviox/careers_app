from django.urls import path
from .api import CandidateViewset

app_name = "candidate_app"

urlpatterns = [
    path("search/<str:email>/<str:number>", CandidateViewset.as_view({"get": "search_by_email"}), name="search"),
]
# 