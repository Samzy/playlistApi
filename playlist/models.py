from django.db import models
from django.contrib.auth.models import User


class Playlist(models.Model):
    title = models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
