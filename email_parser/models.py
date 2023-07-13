from django.core.validators import MaxValueValidator, MinValueValidator
from djongo import models
from djongo.storage import GridFSStorage

grid_fs_storage = GridFSStorage(collection='newspaper', base_url='https://100043.pythonanywhere.com/media/')


class Event(models.Model):
    title = models.CharField(max_length=500)
    link = models.URLField(max_length=2048)
    linkedin = models.URLField(max_length=2048)
    twitter = models.URLField(max_length=2048)
    facebook = models.URLField(max_length=2048)
    post_date = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, null=True, blank=True)
    venue = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254, null=True, blank=True)
    tagline = models.TextField(max_length=500, null=True, blank=True)
    vanue_page_link = models.URLField(max_length=2048, null=True, blank=True)
    organiser_website = models.URLField(max_length=2048, null=True, blank=True)
    organiser_email = models.EmailField(max_length=254, null=True, blank=True)
    website = models.URLField(max_length=2048, null=True, blank=True)
    TYPE_CHOICES = [
        ("Offline", 'Offline only'),
        ("Online", 'Online only'),
        ("Hybrid", 'Hybrid'),
    ]
    type = models.CharField(max_length=50, choices=TYPE_CHOICES, null=True, blank=True)
    EVENT_CHOICES = [
        ("Trade_show", 'Trade show'),
        ("Webinar", 'Webinar'),
        ("Conference", 'Conference'),
    ]
    event_category = models.CharField(max_length=30, choices=EVENT_CHOICES, null=True, blank=True)
    business_category = models.TextField(max_length=1000, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    instagram = models.URLField(blank=True, null=True, max_length=2048)
    youtube = models.URLField(blank=True, null=True, max_length=2048)
    tiktok = models.URLField(blank=True, null=True, max_length=2048)
    hashtag = models.CharField(max_length=200, null=True, blank=True)
    mention = models.CharField(max_length=200, null=True, blank=True)
    visitors_number = models.IntegerField(validators=[MaxValueValidator(99999), MinValueValidator(1)], null=True,
                                          blank=True)
    exhibitors_number = models.IntegerField(validators=[MaxValueValidator(99999), MinValueValidator(1)], null=True,
                                            blank=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    # visitors_number = models.CharField(max_length=200, null = True, blank = True)
    # exhibitors_number = models.CharField(max_length=200, null = True, blank = True)
    logo = models.ImageField(upload_to='', storage=grid_fs_storage, null=True, blank=True)
    exhibitor_creator_list = models.EmailField(max_length=254, null=True, blank=True)
    exhibitor_list = models.URLField(max_length=2048, null=True, blank=True)
    exhibitor_form = models.URLField(max_length=2048, null=True, blank=True)
    opportunities = models.CharField(max_length=1000, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    BDEventID = models.IntegerField(null=True, blank=True)
    STATUS_CHOICES = [
        ("Complete", 'Complete'),
        ("InProgress", 'InProgress'),
        ("Error", 'Error'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, null=True, blank=True)
    venue_website = models.URLField(max_length=2048, null=True, blank=True)
    PROMOTION_CHOICES = [
        ("Mail", 'Mail only'),
        ("Offline", 'Offline only'),
        ("Online", 'Online only'),
        ("No", 'No'),
        ("Hybrid", 'Hybrid'),
    ]
    promotion = models.CharField(max_length=20, choices=PROMOTION_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.title
