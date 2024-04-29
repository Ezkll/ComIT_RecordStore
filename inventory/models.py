import uuid
from django.db import models

# Create your models here.
class Artist(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    bio = models.TextField(max_length=1000)
    def __str__(self):
        return self.name
    
class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='albums')
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    rating = models.IntegerField()
#   num_stars = models.IntegerField()
#   num_copies = models.IntegerField()
#   album_cover = models.ImageField(upload_to='album_covers/', blank=True)
    def __str__(self):
        return self.title