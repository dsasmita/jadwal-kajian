from django.db import models

class Ustad(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True)
    profile_excerpt = models.CharField(max_length=256, null=True, blank=True)
    profile = models.TextField(null=True, blank=True)
    link_youtube = models.CharField(max_length=256, null=True, blank=True)
    link_fb = models.CharField(max_length=256, null=True, blank=True)
    link_instagram = models.CharField(max_length=256, null=True, blank=True)
    link_twitter = models.CharField(max_length=256, null=True, blank=True)
    photo = models.ImageField(null=True, blank=True, upload_to='ustad')
    def __str__(self):
        return self.name

class Province(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True)
    def __str__(self):
        return self.name

class City(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    name = models.CharField(max_length=256, null=True, blank=True)
    def __str__(self):
        return self.name

class Mosque(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=256, null=True, blank=True)
    postal_code = models.CharField(max_length=256, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

