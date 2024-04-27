from django.http import HttpRequest
from django.shortcuts import render
from django.views import View
from inventory.models import Album, Artist

# Create your views here.
class ArtistView(View):
    def get(self, request: HttpRequest):
        artists = Artist.objects.all()
        context = {
            'artists': artists
        }       
        return render(request = request, template_name='artist_list.html', context=context)

class AlbumView(View):
    def get(self, request: HttpRequest):
        albums = Album.objects.all()
        context = {
            'albums': albums
        }
        return render(request = request, template_name='album_list.html', context=context)
                      
