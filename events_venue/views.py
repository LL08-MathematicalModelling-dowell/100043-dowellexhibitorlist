from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Event


def index(request):
    return render(request, 'events_venue/form.html')


def multistepformexample_save(request):
    if request.method != "POST":
        return HttpResponseRedirect(reverse("events_venue:main-view"))
    else:
        email = request.POST.get("email")
        name = request.POST.get("name")
        venue = request.POST.get("venue")
        tagline = request.POST.get("tagline")
        vanue_page_link = request.POST.get("vanue_page_link")
        organiser_website = request.POST.get("organiser_website")
        organiser_email = request.POST.get("organiser_email")
        website = request.POST.get("website")
        exhibitor = request.POST.get("exhibitor")
        type = request.POST.get("type")
        category = request.POST.get("category")
        business_category = request.POST.get("business_category")
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")
        linkedin = request.POST.get("linkedin")
        twitter = request.POST.get("twitter")
        facebook = request.POST.get("facebook")
        instagram = request.POST.get("instagram")
        youtube = request.POST.get("youtube")
        tiktok = request.POST.get("tiktok")
        hashtag = request.POST.get("hashtag")
        mention = request.POST.get("mention")
        visitors_number = request.POST.get("visitors_number")
        exhibitors_number = request.POST.get("exhibitors_number")
        description = request.POST.get("description")
        logo_image = request.FILES['logo'] if 'logo' in request.FILES else None

        if logo_image:
            # save attatched logo
            # create a new instance of FileSystemStorage
            fs = FileSystemStorage()
            file = fs.save(logo_image.name, logo_image)
            # the fileurl variable now contains the url to the file. This can be used to serve the file when needed.
            logo = file
        try:
            Event.objects.create(
                email=email,
                name=name,
                venue=venue,
                tagline=tagline,
                vanue_page_link=vanue_page_link,
                organiser_website=organiser_website,
                organiser_email=organiser_email,
                website=website,
                exhibitor=exhibitor,
                type=type,
                category=category,
                business_category=business_category,
                start_date=start_date,
                end_date=end_date,
                visitors_number=visitors_number,
                exhibitors_number=exhibitors_number,
                linkedin=linkedin,
                twitter=twitter,
                facebook=facebook,
                instagram=instagram,
                youtube=youtube,
                tiktok=tiktok,
                hashtag=hashtag,
                mention=mention,
                description=description,
                logo=logo
            )
            messages.success(request, "Event Saved Successfully, Thank you.")
            return HttpResponseRedirect(reverse('events_venue:thanks'))
        except:
            messages.error(request, "Error in Saving Event")
            return HttpResponseRedirect(reverse('events_venue:thanks'))


def response_recorded(request):
    return render(request, 'events_venue/thanks.html')
