from django.shortcuts import render
from api.models import Search, SongPlay

# Create your views here.
def main_dashboard(request):
    searches = Search.objects.all().order_by('-num_searches')[:10].values()
    songplays = SongPlay.objects.all().order_by('-num_plays')[:10].values()
    return render(request, 'app/main.html', { 'searches': searches, 'songplays': songplays })