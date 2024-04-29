from django.contrib import admin
from inventory.models import Album, Artist


# Register your models here.
class AlbumAdmin(admin.ModelAdmin):
    """Admin interface customization for the Album model."""

    list_display = ('id', 'title', 'artist', 'release_date', 'rating')
    # list_filter = ('artist', 'release_date')
    # search_fields = ('title', 'artist__name')


class ArtistAdmin(admin.ModelAdmin):
    """Admin interface customization for the Artist model."""

    list_display = ('id', 'name', 'bio')
    # search_fields = ('name', 'bio')

admin.site.register(Album, AlbumAdmin) 
admin.site.register(Artist, ArtistAdmin)



