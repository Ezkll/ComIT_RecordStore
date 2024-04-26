### ComIT_RecordStore
> ComIT Course Sample Project App

This app is a record store for music and albums. It is built using the Django framework, with SQLite as the database and Python as the programming language.

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


### URLS.PY Steps




