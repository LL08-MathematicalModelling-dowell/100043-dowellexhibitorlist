import base64
import csv
import json
import os

import gridfs
import requests
from PIL import Image
from bson.objectid import ObjectId
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test, login_required
from django.core.mail import BadHeaderError
from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mass_mail
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from pymongo import MongoClient

from event.models import Details
from .models import Exhibitor


# helper functions
def send_email(to_email):
    subject = settings.MAIL_SUBJECT
    from_email = settings.EMAIL_HOST_USER
    to = to_email
    text_content = f"{user} is using Armify and has noted that your Email is not yet registered with an armify account. Please go to 'https://www.finalDomain.com' and register for an account."
    html_content = f'<p><strong>{user}</strong> is using <strong>Armify</strong> and has noted that your Email is not yet registered with an armify account. Please go to <strong>https://www.finalDomain.com</strong> and register for an account.</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    try:
        msg.send()
    except BadHeaderError:
        print('Invalid header found.')


# Create your views here.
def index(request):
    try:
        print("ssssssssssssssssssssssssssssssssssss")
        session_id = request.GET.get('session_id', None)
        if session_id:
            request.session["session_id"] = str(session_id)
            print("ssssssssssssssssssssssssssssssssssss", request.session["session_id"])
            return render(request, 'exhibitors/form1.html', {"session_id": session_id})
        if 'user_exhibitor' not in request.session:
            session_id = request.GET.get('session_id', None)
            if session_id:
                url = "http://100002.pythonanywhere.com/"
                # adding eddited field in article
                payload = json.dumps({
                    "cluster": "login",
                    "database": "login",
                    "collection": "login",
                    "document": "login",
                    "team_member_ID": "6752828281",
                    "function_ID": "ABCDE",
                    "command": "fetch",
                    "field": {"SessionID": session_id},
                    "update_field": "nil",
                    "platform": "bangalore"
                })
                headers = {
                    'Content-Type': 'application/json'
                }

                response = requests.request("POST", url, headers=headers, data=payload)
                data = json.loads(response.text)
                # context["username"]=data[0]["Username"]
                request.session['user_exhibitor'] = data['data'][0]["Username"]
                return render(request, 'exhibitors/form1.html')
            else:
                return redirect("https://100014.pythonanywhere.com/d_login")
        else:
            return render(request, 'exhibitors/form1.html')

    except:
        return redirect("https://100014.pythonanywhere.com/d_login")
    # return render(request, 'exhibitors/form1.html')


def validate_email_using_dowell_sso(email):
    url = "https://100085.pythonanywhere.com/api/validate-exhibitor-email/"

    payload = json.dumps({
        "email": email
    })
    headers = {
        'Content-Type': 'application/json'
    }

    try:
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response)
        response_json = response.json()
        success = response_json.get('success', False)
        return success
    except requests.exceptions.RequestException as e:
        return False
    except ValueError as e:
        return False


def multistepform1_save(request):
    if request.method != "POST":
        return HttpResponseRedirect(reverse("exhibitors:main-view"))
    else:
        email = request.POST.get("email")

        if not validate_email_using_dowell_sso(email):
            messages.error(request, "The email is not valid, Exhibitor can not be created!")
            return HttpResponseRedirect(reverse('exhibitors:thanks'))

        event = Details.objects.filter(exhibitor_creator_list=email)
        event_length = len(event)
        complete = 0
        # print(event)
        for eve in range(event_length):
            if event[eve].status == "Complete":
                complete = 1
            elif event[eve].status == "InProgress":
                complete = 0
                return render(request, 'exhibitors/form2.html', {'email': email,
                                                                 'event': event[eve]})
            elif event[eve].status == "Error":
                messages.error(request, "Sorry Event status is Error, Exhibitor can not be created!")
                return HttpResponseRedirect(reverse('exhibitors:thanks'))
        if complete == 1:
            return render(request, 'exhibitors/event_details.html', {'obj': event[0]})
        # if event:
        #     if event[0].status == "Complete":
        #         return render(request, 'exhibitors/event_details.html',{'obj':event[0]})
        #     if event[0].status == "InProgress":
        #         return render(request, 'exhibitors/form2.html',{'email':email,
        #                                                         'event':event[0]})
        #     else:
        #         messages.error(request,"Sorry Event status is Error, Exhibitor can not be created!")
        #         return HttpResponseRedirect(reverse('exhibitors:thanks'))
        else:
            messages.error(request, "Sorry No record found, Exhibitor can not be created!")
            return HttpResponseRedirect(reverse('exhibitors:thanks'))


def multistepform2_save(request):
    if request.method != "POST":
        return HttpResponseRedirect(reverse("exhibitors:main-view"))
    else:
        BDEventID = request.POST.get("eventid")
        email = request.POST.get("email")
        name = request.POST.get("name")
        brand_name = request.POST.get("brand_name")
        name_incharge = request.POST.get("name_incharge")
        designation_incharge = request.POST.get("designation_incharge")
        exhibitor_page_link = request.POST.get("exhibitor_page_link")
        exhibitor_website = request.POST.get("exhibitor_website")
        exhibitor_email = request.POST.get("exhibitor_email")
        exhibitor_both_number = request.POST.get("exhibitor_both_number")
        exhibitor_city = request.POST.get("exhibitor_city")
        exhibitor_country = request.POST.get("exhibitor_country")
        exhibitor_address = request.POST.get("exhibitor_address")
        type = request.POST.get("type")
        exhibitor_product = request.POST.get("exhibitor_product")
        linkedin = request.POST.get("linkedin")
        twitter = request.POST.get("twitter")
        facebook = request.POST.get("facebook")
        instagram = request.POST.get("instagram")
        youtube = request.POST.get("youtube")
        tiktok = request.POST.get("tiktok")
        hashtag = request.POST.get("hashtag")
        mention = request.POST.get("mention")
        description = request.POST.get("description")
        comments = request.POST.get("comments")
        logo_image = request.FILES['logo'] if 'logo' in request.FILES else None

        if not validate_email_using_dowell_sso(email):
            messages.error(request, "The email is not valid, Exhibitor can not be created!")
            return HttpResponseRedirect(reverse('exhibitors:thanks'))

        if logo_image:
            # save attatched logo
            # create a new instance of FileSystemStorage
            # fs = FileSystemStorage()
            string = 'mongodb+srv://qruser:4q5ubxjxe91bzkx548qhu@cluster0.n2ih9.mongodb.net/DB_IMAGE?retryWrites=true&w=majority'
            connection = MongoClient(string)
            db = connection.exhibitor_details
            fs = gridfs.GridFS(db, collection='fs')
            # saving image in mongo db
            file = fs.put(logo_image, filename=logo_image.name, email=email,
                          name=name,
                          brand_name=brand_name,
                          name_incharge=name_incharge,
                          designation_incharge=designation_incharge,
                          exhibitor_page_link=exhibitor_page_link,
                          exhibitor_website=exhibitor_website,
                          exhibitor_email=exhibitor_email,
                          exhibitor_both_number=exhibitor_both_number,
                          exhibitor_city=exhibitor_city,
                          exhibitor_country=exhibitor_country,
                          exhibitor_address=exhibitor_address,
                          type=type,
                          exhibitor_product=exhibitor_product,
                          linkedin=linkedin,
                          twitter=twitter,
                          facebook=facebook,
                          instagram=instagram,
                          youtube=youtube,
                          tiktok=tiktok,
                          hashtag=hashtag,
                          mention=mention,
                          BDEventID=BDEventID,
                          description=description,
                          comments=comments, )
        form = {
            "email": email,
            "name": name,
            "brand_name": brand_name,
            "name_incharge": name_incharge,
            "designation_incharge": designation_incharge,
            "exhibitor_page_link": exhibitor_page_link,
            "exhibitor_website": exhibitor_website,
            "exhibitor_email": exhibitor_email,
            "exhibitor_both_number": exhibitor_both_number,
            "exhibitor_city": exhibitor_city,
            "exhibitor_country": exhibitor_country,
            "exhibitor_address": exhibitor_address,
            "type": type,
            "exhibitor_product": exhibitor_product,
            "linkedin": linkedin,
            "twitter": twitter,
            "facebook": facebook,
            "instagram": instagram,
            "youtube": youtube,
            "tiktok": tiktok,
            "hashtag": hashtag,
            "mention": mention,
            "description": description,
            "comments": comments,
            "BDEventID": BDEventID,
            # "url_generated": "https://npslive.org/elementor-211/?utmcode="+ brand_name,
            "logo": logo_image,
        }
        # mail(form)
        # creating a image object (main image)
        try:
            im1 = Image.open(logo_image)
            image_ex = logo_image.name
            image_ex = image_ex.split(".")
            image_name = "image." + image_ex[1]
            # save a image using extension
            script_directory = os.path.dirname(os.path.abspath(__file__))
            data_file = os.path.join(script_directory, image_name)
            im1 = im1.save(data_file)
            print(data_file)
            # THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
            image_path = os.path.join(script_directory, image_name)
            print(image_path)
            # image_path = "home/100043/"+image_name
            # print(image_path)
            with open(image_path, "rb") as image_file:
                logo_image_encoded = base64.b64encode(image_file.read())
                print("Logo image encoded")
                with open("imageToSave.png", "wb") as fh:
                    fh.write(base64.decodebytes(logo_image_encoded))
                # print(logo_image_encoded)
            # logo_image_encoded = base64.b64encode(imageCopy.read())
            # logo_image_encoded = base64.b64encode(logo_image.read())
        except Exception as ex:
            print('hahahha', ex)
            messages.error(request, "There is an error with the image you've uploaded, try using another image")
            return HttpResponseRedirect(reverse('exhibitors:thanks'))

        try:
            # connecting with mongodb through function in views.py file
            url = 'http://100002.pythonanywhere.com/'
            data = {
                "cluster": "exhibitor",
                "database": "exhibitor",
                "collection": "exhibitors_exhibitor",
                "document": "exhibitor",
                "team_member_ID": "2378987",
                "function_ID": "ABCDE",
                "command": "insert",
                "field": {
                    # "created": timezone.now,
                    "email": email,
                    "name": name,
                    "brand_name": brand_name,
                    "name_incharge": name_incharge,
                    "designation_incharge": designation_incharge,
                    "exhibitor_page_link": exhibitor_page_link,
                    "exhibitor_website": exhibitor_website,
                    "exhibitor_email": exhibitor_email,
                    "exhibitor_both_number": exhibitor_both_number,
                    "exhibitor_city": exhibitor_city,
                    "exhibitor_country": exhibitor_country,
                    "exhibitor_address": exhibitor_address,
                    "type": type,
                    "exhibitor_product": exhibitor_product,
                    "linkedin": linkedin,
                    "twitter": twitter,
                    "facebook": facebook,
                    "instagram": instagram,
                    "youtube": youtube,
                    "tiktok": tiktok,
                    "hashtag": hashtag,
                    "mention": mention,
                    "description": description,
                    "comments": comments,
                    "BDEventID": BDEventID,
                    "logo": str(logo_image_encoded),
                },

                'update_field': {
                    "name": "Joy update",
                    "phone": "123456",
                    "age": "26",
                    "language": "Englis",

                },
                "platform": "bangalore",

            }
            headers = {'content-type': 'application/json'}

            response = requests.post(url, json=data, headers=headers)
            messages.success(request, "Exhibitor Saved Successfully, Thank you.")
            return HttpResponseRedirect(reverse('exhibitors:thanks'))
        except:
            messages.error(request, "Error in Saving Exhibitor")
            return HttpResponseRedirect(reverse('exhibitors:thanks'))


def response_recorded(request):
    return render(request, 'exhibitors/thanks.html')


def event_details(request):
    return render(request, 'exhibitors/event_details.html')


@login_required(login_url='/accounts/login/')
def create_email(request):
    return render(request, 'exhibitors/create_email.html')


@login_required(login_url='/accounts/login/')
def send_email(request):
    if request.method != "POST":
        return HttpResponseRedirect(reverse("exhibitors:main-view"))
    else:
        subject = request.POST.get("subject")
        content = request.POST.get("content")
        link = request.POST.get("link")
        email_list = list(Exhibitor.objects.values_list('exhibitor_email', flat=True))
        message = content + '\n' + link
        email_from = settings.EMAIL_HOST_USER
        recipient_list = email_list
        # print(subject, content, link)
        mes = ()
        # print(email_list)
        for i in range(len(recipient_list)):
            mes = mes + ((subject, message, email_from, [recipient_list[i]]),)
        # print(mes)
        # mes = mes + ((subject, message, email_from, ["anjanas@dowellresearch.in"]) , )
        send_mass_mail(mes, fail_silently=False)

    return render(request, 'exhibitors/send_email.html')


@login_required()
@user_passes_test(lambda u: u.is_superuser)
def files_ListView(request):
    string = settings.MONGODB_CONN
    connection = MongoClient(string)
    db = connection['exhibitor_details']
    collection = db['fs.files']
    file = []
    for doc in collection.find({}):
        # print(doc)
        file.append(doc)
    # print(file)
    file.reverse()
    # finding event name
    db = connection['events_details']
    collection = db['event_details']
    paginator = Paginator(file, 100)  # Show 100 files per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    for i in range(len(page_obj)):
        if "BDEventID" in page_obj[i]:
            event_name = collection.find_one({"BDEventID": int(page_obj[i]['BDEventID'])}, {"_id": 0, "name": 1})
            if event_name is None:
                # print(event_name['name'])
                continue
            page_obj[i]['event_name'] = event_name['name']
            # except:
            #     event_name = collection.find_one( {"BDEvent_ID" : int(page_obj[i]['BDEventID'])}, {"_id" : 0, "Name of the event" :1 } )
            # page_obj[i]['event_name']=event_name['name']
    return render(request, 'exhibitors/file_list.html', {'page_obj': page_obj})


@login_required(login_url='/accounts/login/')
@user_passes_test(lambda u: u.is_superuser)
def files_ListSearchView(request):
    if request.method == "POST":
        search_text = request.POST.get("search_text")
        # Saving the search parameters on the session
        request.session['search_text'] = search_text

    string = settings.MONGODB_CONN
    connection = MongoClient(string)
    db = connection['exhibitor_details']
    collection = db['fs.files']
    file = []
    {'$regex': request.session['search_text'] + '.*'}
    # for doc in collection.find({"email": request.session['email']}):
    for doc in collection.find(
            {"$or": [
                {"email": request.session['search_text']},
                # {"name": {'$regex' : request.session['search_text'] + '.*'}},
                {"name": request.session['search_text']},
                {"name": request.session['search_text'] + ' '},
                {"brand_name": request.session['search_text']},
                {"brand_name": request.session['search_text'] + ' '},
            ]}
    ):
        file.append(doc)
    # print(file)
    file.reverse()
    db = connection['events_details']
    collection = db['event_details']
    paginator = Paginator(file, 100)  # Show 100 files per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    for i in range(len(page_obj)):
        if "BDEventID" in page_obj[i]:
            event_name = collection.find_one({"BDEventID": int(page_obj[i]['BDEventID'])}, {"_id": 0, "name": 1})
            if event_name is None:
                continue
            page_obj[i]['event_name'] = event_name['name']
    return render(request, 'exhibitors/file_search.html', {'page_obj': page_obj})


@login_required(login_url='/accounts/login/')
@user_passes_test(lambda u: u.is_superuser)
def files_DetailView(request, id):
    string = settings.MONGODB_CONN
    connection = MongoClient(string)
    db = connection['exhibitor_details']
    collection = db['fs.files']
    file = collection.find_one({'_id': ObjectId(id)})
    return render(request, 'exhibitors/file_detail.html', {'file': file})


@login_required(login_url='/accounts/login/')
@user_passes_test(lambda u: u.is_superuser)
def file_DeleteView(request, id):
    string = settings.MONGODB_CONN
    connection = MongoClient(string)
    db = connection['exhibitor_details']
    collection_files = db['fs.files']
    collection_files.delete_one({'_id': ObjectId(id)})
    collection_chunks = db['fs.chunks']
    collection_chunks.delete_many({'files_id': ObjectId(id)})
    message = "File details with ID:" + id + " has been deleted"
    return render(request, 'exhibitors/file_message.html', {'message': message})


@login_required(login_url='/accounts/login/')
@user_passes_test(lambda u: u.is_superuser)
def file_UpdateView(request, id):
    if request.method != "POST":
        return HttpResponseRedirect(reverse("exhibitors:file-list-view"))
    else:
        BDEventID = request.POST.get("BDEventID")
        email = request.POST.get("email")
        name = request.POST.get("name")
        brand_name = request.POST.get("brand_name")
        name_incharge = request.POST.get("name_incharge")
        designation_incharge = request.POST.get("designation_incharge")
        exhibitor_page_link = request.POST.get("exhibitor_page_link")
        exhibitor_website = request.POST.get("exhibitor_website")
        exhibitor_email = request.POST.get("exhibitor_email")
        exhibitor_both_number = request.POST.get("exhibitor_both_number")
        exhibitor_city = request.POST.get("exhibitor_city")
        exhibitor_country = request.POST.get("exhibitor_country")
        exhibitor_address = request.POST.get("exhibitor_address")
        type = request.POST.get("type")
        exhibitor_product = request.POST.get("exhibitor_product")
        linkedin = request.POST.get("linkedin")
        twitter = request.POST.get("twitter")
        facebook = request.POST.get("facebook")
        instagram = request.POST.get("instagram")
        youtube = request.POST.get("youtube")
        tiktok = request.POST.get("tiktok")
        hashtag = request.POST.get("hashtag")
        mention = request.POST.get("mention")
        description = request.POST.get("description")
        comments = request.POST.get("comments")

    string = settings.MONGODB_CONN
    connection = MongoClient(string)
    db = connection['exhibitor_details']
    collection_files = db['fs.files']
    collection_files.update_one({'_id': ObjectId(id)}, {"$set": {"email": email, "name": name, "brand_name": brand_name,
                                                                 "name_incharge": name_incharge,
                                                                 "designation_incharge": designation_incharge,
                                                                 "exhibitor_page_link": exhibitor_page_link,
                                                                 "exhibitor_website": exhibitor_website,
                                                                 "exhibitor_email": exhibitor_email,
                                                                 "exhibitor_both_number": exhibitor_both_number,
                                                                 "exhibitor_city": exhibitor_city,
                                                                 "exhibitor_country": exhibitor_country,
                                                                 "exhibitor_address": exhibitor_address,
                                                                 "type": type,
                                                                 "exhibitor_product": exhibitor_product,
                                                                 "linkedin": linkedin,
                                                                 "twitter": twitter,
                                                                 "facebook": facebook,
                                                                 "instagram": instagram,
                                                                 "youtube": youtube,
                                                                 "tiktok": tiktok,
                                                                 "hashtag": hashtag,
                                                                 "mention": mention,
                                                                 "BDEventID": BDEventID,
                                                                 "description": description,
                                                                 "comments": comments, }})
    message = "File details with ID:" + id + " has been updated"
    return render(request, 'exhibitors/file_message.html', {'message': message})


@login_required(login_url='/accounts/login/')
@user_passes_test(lambda u: u.is_superuser)
def file_exportview(request):
    # if request.method!="POST":
    #     return HttpResponseRedirect(reverse("exhibitors:file-list-view"))
    # else:
    email = request.POST.get("email")
    print(email)
    # return render(request, 'exhibitors/form1.html')
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="files.csv"'

    # script_directory = os.path.dirname(os.path.abspath(__file__))
    # data_file = os.path.join(script_directory, image_name)

    # writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    fields = ['_id', 'email', 'name', 'brand_name', 'name_incharge', 'designation_incharge', 'exhibitor_page_link',
              'exhibitor_website', 'exhibitor_email',
              'exhibitor_both_number', 'exhibitor_city', 'exhibitor_country', 'exhibitor_address', 'type',
              'exhibitor_product', 'linkedin', 'twitter', 'facebook', 'instagram', ' youtube',
              'tiktok', 'hashtag', 'mention', 'BDEventID', 'description', 'comments', 'filename', 'md5', 'chunkSize',
              'length', 'uploadDate']
    writer = csv.DictWriter(response, fieldnames=fields)
    writer.writeheader()
    string = settings.MONGODB_CONN
    connection = MongoClient(string)
    db = connection['exhibitor_details']
    collection = db['fs.files']
    files = []
    # for doc in collection.find({"email": request.session['email']}):
    for doc in collection.find({"email": email},
                               {'_id': 1, 'filename': 1, 'md5': 1, 'chunkSize': 1, 'length': 1, 'uploadDate': 1,
                                'email': 1, 'name': 1, 'brand_name': 1, 'name_incharge': 1,
                                'designation_incharge': 1, 'exhibitor_page_link': 1, 'exhibitor_website': 1,
                                'exhibitor_email': 1,
                                'exhibitor_both_number': 1, 'exhibitor_city': 1, 'exhibitor_country': 1,
                                'exhibitor_address': 1, 'type': 1, 'exhibitor_product': 1, 'linkedin': 1, 'twitter': 1,
                                'facebook': 1, 'instagram': 1, ' youtube': 1,
                                'tiktok': 1, 'hashtag': 1, 'mention': 1, 'BDEventID': 1, 'description': 1,
                                'comments': 1, }):
        files.append(doc)
    files.reverse()

    # writer.writerow(['_id', 'email', 'name', 'brand_name', 'name_incharge', 'designation_incharge', 'exhibitor_page_link', 'exhibitor_website', 'exhibitor_email',
    # 'exhibitor_both_number','exhibitor_city','exhibitor_country','exhibitor_address','type','exhibitor_product','linkedin','twitter','facebook','instagram',' youtube',
    # 'tiktok','hashtag','mention','BDEventID','description','filename','Md5','Chunk Size', 'Length','Upload Date'])

    for file in files:
        # print(file)
        writer.writerow(file)

    print("response", response)
    return response
