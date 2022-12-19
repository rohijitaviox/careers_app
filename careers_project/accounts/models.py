from django.db import models
from django.contrib.auth import get_user_model
import uuid 

User = get_user_model()

class ResetToken(models.Model):
    id = models.UUIDField(primary_key = True,
         default = uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    expired_at = models.DateTimeField(null=True)
    