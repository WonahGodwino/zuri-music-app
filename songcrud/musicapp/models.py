from asyncio.windows_events import NULL
from email.policy import default
from enum import unique
from pickle import TRUE
from pyexpat import model
from django.db import models

# Create your models here.
class Artiste(models.Model):
    artiste_id = models.CharField(max_length=25,primary_key=True, serialize=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField(default= NULL)
    

class Song(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField() 
    likes = models.DateField(max_length=50)
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)



class Lyric(models.Model):
    content = models.CharField(max_length=255)
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
    
   