from django.db import models


class Job(models.Model):

    jobtitle = models.CharField(max_length=255, unique=True)
    job_description = models.TextField(blank=True)
    min_experience = models.CharField(max_length=255)
    max_experience = models.CharField(max_length=255)
    salary_min_lpa = models.CharField(max_length=255)
    salary_max_lpa = models.CharField(max_length=255)
    total_position = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.jobtitle


class Platform(models.Model):

    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class PostLocation(models.Model):

    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    location = models.ForeignKey(Platform, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self) -> str:
        return self.location
