from django.urls import path
from inventory.views import AlbumListView, ArtistDetailView, ArtistListView


urlpatterns = [
    path("artists/", ArtistListView.as_view(), name="artist-list"),
    path("albums/", AlbumListView.as_view(), name="albums"),
    path(
        "<uuid:pk>/", ArtistDetailView.as_view(), name="artist-detail"
    ),
]

# URL will be inventory/home/ because of the include('inventory.urls') in RecordStore/urls.py
# URL in RecordsStore/urls.py is inventory/ because of the path('inventory/', include('inventory.urls')) in RecordStore/urls.py
# Then it will look for the path('home/', home, name='home') in inventory/urls.py
# The view home is imported from inventory/views.py
# The view home will return an HttpResponse object with the content 'Hello, World!' when called
