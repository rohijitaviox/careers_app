"""careers_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.urls import re_path 
from candidate_app.api import CandidateViewset
from rest_framework.routers import SimpleRouter
from jobpost_app.api import JobsViewset, InterviewViewset
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


router = SimpleRouter()

router.register(r'candidate',CandidateViewset)
router.register(r'jobs', JobsViewset)
router.register(r'jobinterview', InterviewViewset)


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
   ),
   public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include([
        re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        path('accounts/',include('accounts.urls')),
        path('candidate/',include('candidate_app.urls',namespace='candidate')),
        path('jobs/',include('jobpost_app.urls')),
    ]))
    
]
urlpatterns+=router.urls
