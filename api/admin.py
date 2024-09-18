from django.contrib import admin
from api.models import Search, SongPlay

# Register your models here.
@admin.register(Search)
class SearchAdmin(admin.ModelAdmin):
    list_display = ['id', 'query', 'num_searches']

@admin.register(SongPlay)
class SongPlayAdmin(admin.ModelAdmin):
    list_display = ['song_id', 'title', 'artist_name', 'album_title', 'num_plays']