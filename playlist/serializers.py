from rest_framework import serializers
from playlist.models import Playlist


class PlaylistSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Playlist
        fields = ('id', 'title', 'user')
