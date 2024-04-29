### ComIT_RecordStore
### ComIT Course Sample Project App

> This app is a record store for music and albums. It is built using the Django framework, with SQLite as the database and Python as the programming language.

### Documenting Steps

Create a Repository in GitHub
Clone Repository
Terminal > pipenv --python 3.12
Terminal > pipenv install Django
Terminal > pipenv shell
Terminal > django-admin startproject LetraTo ./
Setup Run and Debug (Python > Django > Manage.py)
Press F5 to run local server
Terminal > git add .
Terminal > git commit -m "setting up virtual environment"
Select Python version in VSCode (lower right) Pipenv Python
Add an item

### Create App
python manage.py startapp inventory
RecordStore settings.py > INSTALLED APPS > 'inventory'
python manage.py makemigrations
python manage.py migrate


### Using the Database
admin.py
Create classes for your models as admin
```class AlbumAdmin(admin.ModelAdmin):
    """Admin interface customization for the Album model."""

class ArtistAdmin(admin.ModelAdmin):
    """Admin interface customization for the Artist model."""
```
Register those admin classes
```
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Album, AlbumAdmin)
```
Create a SuperUser
```
python manage.py createsuperuser
```

### QuerySets


### Templates and URLS.PY
Create HTML Templates
Register Pages

#### Using Include Tags
``` 
{% include 'artist_list_item.html' with artist=artist %}
```
#### Template Inheritance
using base.html
creating a template folder on root
moving base.html to template folder in root
modifying settings.py and adding 'templates' in the DIR section

#### Bootstrap
Download CSS and Javascript
Create a folder for the bootstrap retain the version number
modify settings.py and add
```
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
```
#### TemplateView
From 
```
    def get(self, request: HttpRequest):
        
        artists = Artist.objects.all()
        context = {
            'artists': artists
        }       
        return render(request = request, template_name='artist_list.html', context=context)

  def get(self, request: HttpRequest):
        albums = Album.objects.all()
        context = {
            'albums': albums
        }
        return render(request = request, template_name='album_list.html', context=context)
                      
    def get(self, request: HttpRequest, artist_id):
        artist = Artist.objects.get(pk=artist_id)
        context = {
            'artist': artist
        }
        return render(request = request, template_name='artist_details.html', context=context).
```
To
```
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
```
#### ListView

#### DetailView

#### Form

#### Create

#### Edit



