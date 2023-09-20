from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from djongo import models


class Event(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    email = models.EmailField(max_length=254)
    venue = models.CharField(max_length=254)
    name = models.CharField(max_length=254)
    tagline = models.TextField(max_length=500)
    vanue_page_link = models.URLField(max_length=2048)
    organiser_website = models.URLField(max_length=2048)
    organiser_email = models.EmailField(max_length=254)
    website = models.URLField(max_length=2048)
    exhibitor = models.URLField(max_length=2048,blank=True, null=True)
    type = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    business_category = models.TextField(max_length=1000)
    start_date = models.DateField( auto_now=True, null=True, blank=True)
    end_date = models.DateField(auto_now=True, null=True, blank=True)
    linkedin = models.URLField(blank=True, null=True, max_length=2048)
    twitter = models.URLField(blank=True, null=True, max_length=2048)
    facebook = models.URLField(blank=True, null=True, max_length=2048)
    instagram = models.URLField(blank=True, null=True, max_length=2048)
    youtube = models.URLField(blank=True, null=True, max_length=2048)
    tiktok = models.URLField(blank=True, null=True, max_length=2048)
    hashtag = models.CharField(max_length=200)
    mention = models.CharField(max_length=200)
    visitors_number = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(1)])
    exhibitors_number = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(1)])
    description = models.TextField(max_length=1000)
    logo = models.ImageField(upload_to='')
    exhibitor_creator_list = models.EmailField(max_length=254, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    BDEventID = models.IntegerField(null=True, blank=True)
    STATUS_CHOICES = [
        ("Complete", 'Complete'),
        ("InProgress", 'InProgress'),
        ("Error", 'Error'),
    ]
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('event-details', kwargs={'pk': self.pk})
