from django.db import models

# Create your models here.
class Search(models.Model):
    query = models.CharField(max_length=255)
    num_searches = models.BigIntegerField(default=1)

class SongPlay(models.Model):
    song_id = models.CharField(max_length=20)
    title = models.CharField(max_length=255)
    artist_name = models.CharField(max_length=255)
    album_title = models.CharField(max_length=255)
    num_plays = models.BigIntegerField(default=1)