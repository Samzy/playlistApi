from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings

import requests


class SpotifyUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    access_token = models.CharField(max_length=255)
    refresh_token = models.CharField(max_length=255)
    token_type = models.CharField(max_length=255)
    expires_time = models.DateTimeField()
    scope = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_new_access_token(self):
        if self.expires_time < timezone.now():
            payload = {
                'client_id': settings.SPOTIFY_CLIENT_ID,
                'client_secret': settings.SPOTIFY_CLIENT_SECRET,
                'grant_type': 'refresh_token',
                'refresh_token': self.refresh_token
            }

            r = requests.post('https://accounts.spotify.com/api/token', data=payload)

            if r.status_code != 200:
                return False

            decoded_response = r.json()

            self.access_token = decoded_response['access_token']
            self.scope = decoded_response['scope']
            self.expires_time = timezone.now() + timezone.timedelta(minutes=59)

            self.save()

            return True

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
