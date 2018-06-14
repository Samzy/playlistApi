from rest_framework import serializers
from auth.models import SpotifyUser, YoutubeUser, SoundCloudUser


class SpotifyUserSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = SpotifyUser
        fields = ('id', 'user', 'access_token', 'refresh_token', 'created_at', 'updated_at')


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
