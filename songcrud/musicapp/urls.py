from django.urls import path

from . import views
from .views import Song, ArtistesView, Lyric,view_artiste, add_artistes

urlpatterns = [
    path('', views.index, name='index'),
    path('artistes/', ArtistesView),
    path('view_artist/<int:pk>', view_artiste),
    #path('view_artist/<int:pk>', view_artiste)
    path('add_artistes/', add_artistes)
]