from django.utils import timezone
from djongo import models


# Create your models here.
class Exhibitor(models.Model):
    created = models.DateTimeField(default=timezone.now)
    email = models.EmailField(max_length=256)
    name = models.CharField(max_length=256)
    brand_name = models.CharField(max_length=256)
    name_incharge = models.CharField(max_length=256)
    designation_incharge = models.CharField(max_length=500)
    exhibitor_page_link = models.URLField(max_length=2048, blank=True, null=True)
    exhibitor_website = models.URLField(max_length=2048)
    exhibitor_email = models.EmailField(max_length=256)
    exhibitor_both_number = models.CharField(max_length=500)
    exhibitor_city = models.CharField(max_length=500)
    exhibitor_country = models.CharField(max_length=500)
    exhibitor_address = models.CharField(max_length=500)
    type = models.CharField(max_length=50)
    exhibitor_product = models.CharField(max_length=500)
    linkedin = models.URLField(blank=True, null=True, max_length=2048)
    twitter = models.URLField(blank=True, null=True, max_length=2048)
    facebook = models.URLField(blank=True, null=True, max_length=2048)
    instagram = models.URLField(blank=True, null=True, max_length=2048)
    youtube = models.URLField(blank=True, null=True, max_length=2048)
    tiktok = models.URLField(blank=True, null=True, max_length=2048)
    hashtag = models.CharField(max_length=256)
    mention = models.CharField(max_length=256)
    description = models.TextField(max_length=1000)
    logo = models.ImageField(upload_to='')
    BDEventID = models.IntegerField(null=True, blank=True)


class MailCount(models.Model):
    count = models.IntegerField(default=1)
