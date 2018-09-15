from django.db import models

class Ustad(models.Model):
    name = models.CharField(max_length=256, null=True)
    profile_excerpt = models.CharField(max_length=256, null=True)
    profile = models.TextField(null=True)
    link_youtube = models.CharField(max_length=256, null=True)
    link_fb = models.CharField(max_length=256, null=True)
    link_instagram = models.CharField(max_length=256, null=True)
    link_twitter = models.CharField(max_length=256, null=True)
    photo = models.ImageField(null=True, blank=True, upload_to='ustad')

    def __str__(self):
        return self.name
