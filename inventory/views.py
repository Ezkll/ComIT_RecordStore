from django.http import HttpRequest
from django.shortcuts import render
from django.views import View
from inventory.models import Album, Artist

# Create your views here.
class ArtistListView(View):
    def get(self, request: HttpRequest):
        
        artists = Artist.objects.all()
        context = {
            'artists': artists
        }       
        return render(request = request, template_name='artist_list.html', context=context)

class AlbumListView(View):
    def get(self, request: HttpRequest):
        albums = Album.objects.all()
        context = {
            'albums': albums
        }
        return render(request = request, template_name='album_list.html', context=context)
                      
class ArtistDetailView(View):
    def get(self, request: HttpRequest, artist_id):
        artist = Artist.objects.get(pk=artist_id)
        context = {
            'artist': artist
        }
        return render(request = request, template_name='artist_details.html', context=context)