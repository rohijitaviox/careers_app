from django.contrib import admin
from models_app.models.jobModel import Job
from models_app.models.candidateModel import Candidate
from models_app.models.scheduleInterviewModel import ScheduleInterview

# Register your models here.
admin.site.register(Job)
admin.site.register(Candidate)
admin.site.register(ScheduleInterview)