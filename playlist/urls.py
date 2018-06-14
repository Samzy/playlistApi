from django.conf.urls import url
from playlist import views

urlpatterns = [
    url(r'^$', views.PlaylistView.as_view()),
]