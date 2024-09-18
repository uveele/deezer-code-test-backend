from rest_framework.serializers import ModelSerializer
from api.models import SongPlay

class SongPlaySerializer(ModelSerializer):
    class Meta:
        model = SongPlay
        fields = [
            'id',
            'song_id', 
            'title', 
            'artist_name', 
            'album_title', 
            'num_plays', 
        ]
    
    def create(self, validated_data):
        song_play, created = SongPlay.objects.get_or_create(
            song_id=validated_data.get('song_id'),
            title=validated_data.get('title'),
            artist_name=validated_data.get('artist_name'),
            album_title=validated_data.get('album_title'),
        )
        
        if not created:
            song_play.num_plays += 1
            song_play.save()

        return song_play