import json
import os
from django.shortcuts import render
from django.core.files.storage import default_storage
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.db.models import Q
from events_venue.models import Event

def dowell_purposive_sampling(search_criteria, user_field):
    n = 1000000
    sample_values = []

    # Build a Q object to combine multiple search criteria using OR logic
    q_object = Q()
    for key, value in search_criteria:
        q_object |= Q(**{key: value})

    # Fetch data from the Exhibition model based on the search criteria
    all_data = Event.objects.filter(q_object)

    for item in all_data:
        sample_values.append({
            "timestamp": item.timestamp,
            "email": item.email,
            "venue": item.venue,
            "name": item.name,
            "tagline": item.tagline,
            "venue_page_link": item.vanue_page_link,
            "organiser_website": item.organiser_website,
            "organiser_email": item.organiser_email,
            "website": item.website,
            "exhibitor": item.exhibitor,
            "type": item.type,
            "category": item.category,
            "business_category": item.business_category,
            "start_date": item.start_date,
            "end_date": item.end_date,
            "linkedin": item.linkedin,
            "twitter": item.twitter,
            "facebook": item.facebook,
            "instagram": item.instagram,
            "youtube": item.youtube,
            "tiktok": item.tiktok,
            "hashtag": item.hashtag,
            "mention": item.mention,
            "visitors_number": item.visitors_number,
            "exhibitors_number": item.exhibitors_number,
            "description": item.description,
            "logo": item.logo.url if item.logo else None,
            "exhibitor_creator_list": item.exhibitor_creator_list,
            "city": item.city,
            "country": item.country,
            "BDEventID": item.BDEventID,
            "status": item.status,
        })

        if len(sample_values) == n:
            break

    return sample_values

@csrf_exempt
@api_view(["POST"])
def dowell_search(request):
    if request.method == "POST":
        payload = request.data
        print("payload", payload)
        data_type = payload.get("data_type")
        if data_type == "api":
            search_count = int(payload.get("search_count", 0))
            search_criteria = []
            user_field = payload.get("user_field", {})

            for i in range(search_count):
                key = payload.get(f"key{i}", "")
                value = payload.get(f"value{i}", "")
                search_criteria.append((key, value))

            sample_values = dowell_purposive_sampling(search_criteria, user_field)
            return Response(sample_values)

        elif data_type == "upload":
            print("upload data")
            search_count = int(payload.get("search_count", 0))
            uploaded_data = request.FILES.get("_file")
            user_field = {
                "cluster": "license",
                "database": "license",
                "collection": "licenses",
                "document": "licenses",
                "team_member_ID": "689044433",
                "function_ID": "ABCDE",
                "command": "fetch",
                "field": {},
                "update_field": None,
                "platform": "bangalore",
            }
            search_criteria = []

            for i in range(search_count):
                key = payload.get(f"key{i}", "")
                value = payload.get(f"value{i}", "")
                search_criteria.append((key, value))

            if uploaded_data:
                print("uploaded_data", uploaded_data)
                file_path = default_storage.save(
                    uploaded_data.name, uploaded_data
                )  # Save the uploaded file
                try:
                    with default_storage.open(file_path, "r") as file:
                        json_data = json.load(file)
                        manual_data = json_data
                        sample_values = dowell_purposive_sampling(
                            search_criteria, user_field
                        )
                        return Response(sample_values)
                finally:
                    os.remove(file_path)
        else:
            return Response({"error": "Invalid data type select api or upload"})
    else:
        return Response({"error": "Invalid request method."})

@csrf_exempt
def search(request):
    return render(request, "search_function.html")
