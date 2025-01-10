
from django.db import models

# Create your models here.
class Team(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    photos = models.ImageField(upload_to='photos/%Y/%m/%d', null=True)
    facebook_link = models.URLField(max_length=100, null=True)
    twitter_link = models.URLField(max_length=100, null=True)
    google_link = models.URLField(max_length=100, null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.first_name


