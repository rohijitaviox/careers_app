from django.db import models
from .candidateModel import Candidate
from .jobModel import Job
from .scheduleInterviewModel import ScheduleInterview

class AppliedJob(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applied_by = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self) -> str:
        return self.job