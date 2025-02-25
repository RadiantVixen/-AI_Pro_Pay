from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(
        upload_to="profile_pictures/", null=True, blank=True, default="default.png"
    )
    performance = models.FloatField(default=0)
    language = models.CharField(max_length=10, null=True, blank=True)


