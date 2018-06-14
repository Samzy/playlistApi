from django.db import models
from django.contrib.auth.models import User


class SpotifyUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    accessToken = models.CharField(max_length=255)
    refreshToken = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class YoutubeUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    accessToken = models.CharField(max_length=255)
    refreshToken = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class SoundCloudUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    accessToken = models.CharField(max_length=255)
    refreshToken = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
