from django.urls import path

from . import views
from .views import Song, ArtistesView, Lyric

urlpatterns = [
    path('', views.index, name='index'),
    path('artistes/', ArtistesView)
]