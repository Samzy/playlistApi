from django.shortcuts import render
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from playlist.models import Playlist
from playlist.serializers import PlaylistSerializer


class PlaylistView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_object(self, user_id):
        try:
            return Playlist.objects.filter(user=user_id)
        except Playlist.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        playlist = self.get_object(request.user.id)
        serializer = PlaylistSerializer(playlist, many=True)

        return Response(serializer.data)

    def put(self, request, format=None):
        playlist = self.get_object(request.user.id)
        serializer = PlaylistSerializer(playlist, data=request.data, context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        serializer = PlaylistSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

