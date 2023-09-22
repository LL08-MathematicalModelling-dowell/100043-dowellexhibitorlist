import json
import os
from django.http import JsonResponse
from django.shortcuts import render
from django.core.files.storage import default_storage
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.db.models import Q
from exhibitors.models import Exhibitor


def dowell_purposive_sampling(search_criteria, user_field):
    n = 100000
    sample_values = []

    q_object = Q()
    for key, value in search_criteria:
        q_object |= Q(**{key: value})

    all_data = Exhibitor.objects.filter(q_object)
    print("all_data", all_data)
    for item in all_data:
        sample_values.append(
            {
                "email": item.email,
                "name": item.name,
                "brand_name": item.brand_name,
                "name_incharge": item.name_incharge,
                "designation_incharge": item.designation_incharge,
                "exhibitor_website": item.exhibitor_website,
                "exhibitor_email": item.exhibitor_email,
                "exhibitor_both_number": item.exhibitor_both_number,
                "exhibitor_city": item.exhibitor_city,
                "exhibitor_country": item.exhibitor_country,
                "exhibitor_address": item.exhibitor_address,
                "type": item.type,
                "exhibitor_product": item.exhibitor_product,
                "linkedin": item.linkedin,
                "twitter": item.twitter,
                "facebook": item.facebook,
                "instagram": item.instagram,
                "hashtag": item.hashtag,
                "mention": item.mention,
                "BDEventID": item.BDEventID,
                "description": item.description
            }
        )

        if len(sample_values) == n:
            break
    print("sample_values", sample_values)
    return sample_values


@csrf_exempt
def dowell_search(request):
    if request.method == "POST":
        try:
            payload = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)

        print("payload", payload)
        # data_type = payload.get("data_type")
        # if data_type == "api":
        search_count = int(payload.get("search_count", 0))
        search_criteria = []
        user_field = payload.get("user_field", {})

        for i in range(search_count):
            key = payload.get(f"key{i}", "")
            value = payload.get(f"value{i}", "")
            search_criteria.append((key, value))
        print("search_criteria", search_criteria)
        print("user_field", user_field)
        sample_values = dowell_purposive_sampling(search_criteria, user_field)
        return JsonResponse(sample_values, safe=False)

        # elif data_type == "upload":
        #     print("upload data")
        #     search_count = int(payload.get("search_count", 0))
        #     uploaded_data = request.FILES.get("_file")
        #     user_field = {
        #         "cluster": "license",
        #         "database": "license",
        #         "collection": "licenses",
        #         "document": "licenses",
        #         "team_member_ID": "689044433",
        #         "function_ID": "ABCDE",
        #         "command": "fetch",
        #         "field": {},
        #         "update_field": None,
        #         "platform": "bangalore",
        #     }
        #     search_criteria = []

        #     for i in range(search_count):
        #         key = payload.get(f"key{i}", "")
        #         value = payload.get(f"value{i}", "")
        #         search_criteria.append((key, value))

        #     if uploaded_data:
        #         print("uploaded_data", uploaded_data)
        #         file_path = default_storage.save(
        #             uploaded_data.name, uploaded_data
        #         )  # Save the uploaded file
        #         try:
        #             with default_storage.open(file_path, "r") as file:
        #                 json_data = json.load(file)
        #                 manual_data = json_data
        #                 sample_values = dowell_purposive_sampling(
        #                     search_criteria, user_field
        #                 )
        #                 return JsonResponse(sample_values, safe=False)
        #         finally:
        #             os.remove(file_path)
        # else:
        #     return JsonResponse({"error": "Invalid data type, select api or upload"}, status=400)
    else:
        return JsonResponse({"error": "Invalid request method."}, status=405)


@csrf_exempt
def search(request):
    return render(request, "search_func/search_function.html")


# {"cluster":"license","database":"license","collection":"licenses","document":"licenses","team_member_ID":"689044433","function_ID":"ABCDE","command":"fetch","field":{},"update_field":null,"platform":"bangalore"}
