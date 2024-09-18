from rest_framework.serializers import ModelSerializer
from api.models import Search

class SearchSerializer(ModelSerializer):
    class Meta:
        model = Search
        fields = ['id', 'query', 'num_searches']

    def create(self, validated_data):
        query = validated_data.get('query')
        search, created = Search.objects.get_or_create(query=query.lower())
        
        if not created:
            search.num_searches += 1
            search.save()

        return search
