from django.db import models
from embed_video.fields import EmbedVideoField

# Create your models here.
class Item(models.Model):
    date = models.DateField()
    time = models.TimeField()
    caption = models.CharField(max_length=150)
    video = EmbedVideoField()  # same like models.URLField()