from django.db import models
from .jobModel import Job


class Application(models.Model):

    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    latest_education = models.CharField(max_length=200)
    institute = models.CharField(max_length=255)
    total_experience = models.CharField(max_length=100)
    specific_experience = models.JSONField()
    specific_question = models.JSONField()
    last_ctc = models.IntegerField()
    expected_ctc = models.IntegerField()
    leaving_reason = models.TextField()
    resume = models.FileField(upload_to='/media')
    profiles = models.JSONField()
    jobfound = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name


class Experience(models.model):
    
    applicaition_id = models.ForeignKey(Application, on_delete=models.CASCADE)
    company = models.CharField(max_length=200)
    worked_from = models.DateTimeField(null=True)
    worked_to = models.DateTimeField(null=True)
    last_position = models.DateTimeField(null=True)
    created_at = models.DateField(null=True, auto_now_add=True)
    updated_at = models.DateField(null=True, auto_now=True)

    def __str__(self):
        return self.company


class Project(models.model):

    experience_id = models.ForeignKey(Experience, on_delete=models.CASCADE)
    project_name =  models.CharField()
    description = models.TextField()
    applicant_role = models.TextField()
    tech_stack = models.JSONField()
    links = models.URLField()

    def __str__(self):
        return self.project_name
