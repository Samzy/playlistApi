from rest_framework import serializers
from auth.models import SpotifyUser, YoutubeUser, SoundCloudUser
from django.utils import timezone


def one_hour_plus():
    return timezone.now() + timezone.timedelta(minutes=55)


class SpotifyUserSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    expires_time = serializers.DateTimeField(default=one_hour_plus)

    class Meta:
        model = SpotifyUser
        fields = ('id', 'user', 'access_token', 'refresh_token', 'expires_time', 'scope', 'created_at', 'updated_at')


class SpotifyTokenSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    expires_time = serializers.DateTimeField(default=one_hour_plus)

    class Meta:
        model = SpotifyUser
        fields = ('id', 'user', 'access_token', 'expires_time', 'scope')


class YoutubeUserSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = SpotifyUser
        fields = ('id', 'user', 'access_token', 'refresh_token', 'created_at', 'updated_at')


class SoundCloudUserSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = SpotifyUser
        fields = ('id', 'user', 'access_token', 'refresh_token', 'created_at', 'updated_at')
