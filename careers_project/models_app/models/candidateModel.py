from django.db import models


class Candidate(models.Model):

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    position = models.CharField(max_length=100, null=True)
    profile_pic = models.ImageField(upload_to='media/', null=True)
    higher_education = models.CharField(max_length=200)
    contact_no = models.IntegerField(null=True)
    experience = models.CharField(max_length=100, null=True)
    black_list = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.email
