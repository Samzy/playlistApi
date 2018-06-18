from django.http import Http404
from django.conf import settings
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from auth.serializers import SpotifyUserSerializer, SpotifyTokenSerializer
from auth.models import SpotifyUser

import requests


class SpotifyAuthorise(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        url = 'https://accounts.spotify.com/authorize/'
        url += '?client_id=' + settings.SPOTIFY_CLIENT_ID
        url += '&response_type=code&redirect_uri=' + settings.SPOTIFY_CALLBACK
        url += '&scope=' + ' '.join(settings.SPOTIFY_SCOPE)

        return Response({'AuthUrl': url})


class SpotifyToken(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_object(self, user):
        try:
            return SpotifyUser.objects.get(user=user)
        except SpotifyUser.DoesNotExist:
            raise Http404

    def get(self, request):
        spotifyUser = self.get_object(request.user.id)

        if spotifyUser.expires_time < timezone.now():
            if spotifyUser.get_new_access_token() == False:
                return Response("Error", "Could not refresh access token", status=500)

            serializer = SpotifyTokenSerializer(spotifyUser, context={'request': request})

            return Response(serializer.data)

        else:
            serializer = SpotifyTokenSerializer(spotifyUser, context={'request': request})

            return Response(serializer.data)

    def post(self, request):
        if 'code' in request.data:
            code = request.data['code']
        else:
            raise Http404('Missing Parameter Required')

        if self.get_object(request.user.id).exists():
            return Response({
                'error': 'User has already been associated with a Spotify account'},
                status=status.HTTP_400_BAD_REQUEST
            )

        payload = {
            'client_id': settings.SPOTIFY_CLIENT_ID,
            'client_secret': settings.SPOTIFY_CLIENT_SECRET,
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': settings.SPOTIFY_CALLBACK
        }

        r = requests.post('https://accounts.spotify.com/api/token', data=payload)

        if r.status_code != 200:
            return Response(r.json(), status=500)

        serializer = SpotifyUserSerializer(data=r.json(), context={'request': request})

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)