import json
from django.shortcuts import render
from django.core.files.storage import default_storage
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
import requests


def dowellConnection(data):
    url = "http://100002.pythonanywhere.com/"
    payload = json.dumps(data)
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, data=payload)
    print(response)
    return response.json()

def dowell_purposive_sampling(search_criteria, user_field, manual_data):
    n = 1000000
    sample_values = []
    data = {
        "cluster": user_field.get("cluster", ""),
        "database": "license",
        "collection": "licenses",
        "document": "licenses",
        "team_member_ID": "689044433",
        "function_ID": "ABCDE",
        "command": "fetch",
        "field": {},
        "update_field": None,
        "platform": "bangalore"
    }

    if manual_data:
        all_data = manual_data.get("data", [])
    else:
        response = dowellConnection(data)
        all_data = response.get("data", [])

    for item in all_data:
        # check if all search criteria values are present in the corresponding item's values
        criteria_satisfied = True
        for key, value in search_criteria:
            if key not in item or value not in str(item[key]):
                criteria_satisfied = False
                break
        if criteria_satisfied:
            sample_values.append(item)
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
            manual_data = None
            user_field = payload.get("user_field", {})

            for i in range(search_count):
                key = payload.get(f"key{i}", "")
                value = payload.get(f"value{i}", "")
                search_criteria.append((key, value))

            sample_values = dowell_purposive_sampling(
                search_criteria, user_field, manual_data
            )
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
            manual_data = None

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
                            search_criteria, user_field, manual_data
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