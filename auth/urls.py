from django.urls import path
from django.conf.urls import url, include
from rest_framework.authtoken import views as auth_token_views
from auth import views as auth_views


urlpatterns = [
    url(r'^api-token-auth/', auth_token_views.obtain_auth_token),
    url(r'^spotify/authorise', auth_views.SpotifyAuthorise.as_view()),
    url(r'^spotify/access-token', auth_views.SpotifyToken.as_view())
]