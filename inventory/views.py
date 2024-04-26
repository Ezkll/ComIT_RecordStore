from django.http import HttpRequest
from django.shortcuts import render
from django.views import View
from inventory.models import Artist

# Create your views here.
class ArtistView(View):
    def get(self, request: HttpRequest):
        artists = Artist.objects.all()
        context = {
            'artists': artists
        }       
        return render(request = request, template_name='artists.html', context=context)
                      
