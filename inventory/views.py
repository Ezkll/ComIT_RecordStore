from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from inventory.models import Album, Artist
from django.views.generic import TemplateView, ListView, DetailView
from typing import Any


# Create your views here.
class ArtistListView(ListView):
    template_name = "artist_list.html"
    model = Artist
    paginate_by = 12


class AlbumListView(TemplateView):
    template_name = "album_list.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["albums"] = Album.objects.all()
        return context


class ArtistDetailView(DetailView):
    model = Artist


class CreateArtistView(View):
    def get(self, request):
        context = {"artist": None}
        return render(request, "edit_artist.html", context)

    def post(self, request: HttpRequest):
        name = request.POST.get("artist-name")
        bio = request.POST.get("artist-bio")

        if name:
            new_artist = Artist.objects.create(name=name, bio=bio)
            return redirect("artist-detail", new_artist.id)
        else:
            # Handle the case when the name is empty
            return HttpResponse("Name cannot be empty.")


class UpdateArtistView(View):
    def get(self, request, pk=None):
        artist = None
        if pk:
            artist = get_object_or_404(Artist, pk=pk)
        context = {"artist": artist}
        return render(request, "edit_artist.html", context)

    def post(self, request, pk):
        artist = get_object_or_404(Artist, pk=pk)
        artist.name = request.POST.get("artist-name")
        artist.bio = request.POST.get("artist-bio")
        artist.save()

        return redirect("artist-detail", artist.id)
