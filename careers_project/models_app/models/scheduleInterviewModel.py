from django.db import models
from .jobModel import Job
from .candidateModel import Candidate

STATUS_TYPE = (

    ("SELECTED","SELECTED"),
    ("REJECTED","REJECTED"),
    ("BLACKLISTED","BLACKLISTED"),
    ("UNDERPROCESS","UNDERPROCESS")
)


class ScheduleInterview(models.Model):

    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    current_ctc = models.CharField(max_length=100)
    expected_ctc = models.CharField(max_length=100)
    created_by = models.CharField(max_length=200)
    updated_by = models.CharField(max_length=255)
    link = models.URLField()
    interview_date = models.DateField(null=True)
    expiry_time = models.DateTimeField(null=True)
    status = models.CharField(max_length=50, choices=STATUS_TYPE,default="UNDERPROCESS")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.interview_date
