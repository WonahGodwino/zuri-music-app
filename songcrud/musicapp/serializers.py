from rest_framework import serializers
from .models import  Artiste , Song, Lyric

class ArtisteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artiste
        fields = ['artiste_id', 'first_name', 'last_name', 'age']
    

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['song_id','title','release_date',' likes','artiste_id']



class LyricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lyric
        fields = ['content', 'song_id']
