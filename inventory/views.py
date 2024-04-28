from inventory.models import Album, Artist
from django.views.generic import TemplateView, ListView, DetailView
from typing import Any


# Create your views here.
class ArtistListView(ListView):
    template_name = "artist_list.html"
    model = Artist
    paginate_by = 2


class AlbumListView(TemplateView):
    template_name = "album_list.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["albums"] = Album.objects.all()
        return context


class ArtistDetailView(DetailView):
    model = Artist
    
    # template_name = "artist_details.html"

    # def get_context_data(self, **kwargs) -> dict[str, Any]:
    #     context = super().get_context_data(**kwargs)
    #     context["artist"] = Artist.objects.get(pk=self.kwargs["artist_id"])
    #     return context
