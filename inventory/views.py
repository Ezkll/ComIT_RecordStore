from inventory.models import Album, Artist
from django.views.generic import TemplateView
from typing import Any


# Create your views here.
class ArtistListView(TemplateView):
    template_name = "artist_list.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["artists"] = Artist.objects.all()
        return context


class AlbumListView(TemplateView):
    template_name = "album_list.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["albums"] = Album.objects.all()
        return context


class ArtistDetailView(TemplateView):
    template_name = "artist_details.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["artist"] = Artist.objects.get(pk=self.kwargs["artist_id"])
        return context
