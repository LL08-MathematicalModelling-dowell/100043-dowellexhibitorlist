import mimetypes
import os
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from random import choice
from random import randint

import gridfs
import pymongo
import qrcode
from PIL import Image


# define the scope
def mail(form):
    client_id = randint(100000000000000000000000, 999999999999999999999999)
    client_id = str(client_id)
    brand = form['brand_name']
    name = form['brand_name']
    exhibitor_email = form["exhibitor_email"]
    agent = "Netal Pareek"
    linkedin = form["linkedin"]
    twitter = form["twitter"]
    website = form["exhibitor_website"]
    logo = form["logo"]
    logo_name = logo.name
    image = Image.open(logo)
    baseheight = 50
    hpercent = (baseheight / float(image.size[1]))
    wsize = int((float(image.size[0]) * float(hpercent)))
    image = image.resize((wsize, baseheight), Image.ANTIALIAS)
    script_directory = os.path.dirname(os.path.abspath(__file__))
    # data_file = os.path.join(script_directory, 'logo.png')
    data_file = os.path.join(script_directory, logo_name)
    image.save(data_file)

    # url = "https://auth.videoask.com/oauth/token/"
    url = "https://npslive.org/elementor-211/"

    generated_url = url + '?utmcode=' + brand

    # print(generated_url)
    # data = {'grant_type':'refresh_token',
    #     'refresh_token':'RxpYsDJPKb-1GA3b_BqRvPXX57dqbASW_RZqZn4sT1FSY',
    #     'client_id':'Ja3FLLTgLct0rIQt9eaZzVsNeoClQlvB',
    #     'client_secret':'VPDDS9o3ZjiD8CtiLcU4IRHh-xXFTlp5njzghLyndJU8M-BlPVa57lbgUVAWpl41',
    #     'scope':'openid profile email offline_access'}
    # r = requests.post(url,data=data).json()
    # auth = r['access_token']
    # headers = {
    # 'Authorization': 'Bearer '+auth,
    # 'Content-Type': 'application/json',
    # }
    # #data = '{ "title": "QRcodetesting", "show_contact_name": false, "show_contact_email": false, "show_contact_phone_number": false, "show_consent": false, "requires_contact_name": false, "requires_contact_email": false, "requires_contact_phone_number": false, "requires_consent": false }'
    # #response = requests.post('https://api.videoask.com/forms', headers=headers, data=data).json()
    # response=requests.post('https://api.videoask.com/forms/fc2b06aa-ee48-419b-883c-1c13042dba19/duplicate', headers=headers).json()
    # embed=response['share_url']
    embed = generated_url
    # form_id=response['form_id']
    # #data = '{ "title":"'+str(form_id)+'"}'
    # url = ("https://api.videoask.com/forms/"+form_id)
    title = str(name + client_id)

    payload = {"title": title}

    # response = requests.request("PATCH", url, headers=headers, data=json.dumps(payload))

    qr_big = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H
    )
    if form["name_incharge"] != "NA":
        detail = "Hi " + form["name_incharge"]
    else:
        detail = "Hi"
    qr_big.add_data(embed)

    qr_big.make()
    img_qr_big = qr_big.make_image().convert('RGB')
    bdqr_name = "bdqr" + logo_name
    # img_qr_big.save('bdqr.png')
    img_qr_big.save(bdqr_name)

    # image_path = os.path.join(script_directory, 'logo.png')
    image_path = os.path.join(script_directory, logo_name)
    face = Image.open(image_path)
    pos = ((img_qr_big.size[0] - face.size[0]) // 2, (img_qr_big.size[1] - face.size[1]) // 2)

    # file_name = "bdqr.png"
    file_name = bdqr_name
    img_qr_big.paste(face, pos)
    img_qr_big_file = os.path.join(script_directory, file_name)
    img_qr_big.save(img_qr_big_file)
    os.remove(data_file)

    Sender_Email = "uxlivinglab@dowellresearch.uk"
    Reciever_Email = exhibitor_email
    Password = "bkefonjnfuohhhyc"

    newMessage = MIMEMultipart()
    newMessage['Subject'] = "Let customers reach " + str(name) + " quickly using QR code and give their response"

    newMessage['From'] = Sender_Email
    newMessage['To'] = Reciever_Email
    text = """\

    """
    html = """\
    <html>
    <body>
    <style>

    img.one {
    height: 150%;
    width: 150%;
    }


    </style>



    <p>""" + str(detail) + """,</p>

    <p>Let customers give feedback on """ + str(name) + """ quickly using your exclusive QR code</p>

    <img class="one" src="cid:image1"width="583" height="413">
        <p><b>How it works</b></p>

        <p><span class="tab">     1. Download the attached QR Code</p>

        <p><span class="tab">    2. Display in your website, mobile, physical product or anywhere</p>
        <p><span class="tab">     3. Let customers scan the QR code and give feedback</p>
        <p><span class="tab">     4. You can login and see reports in www.uxlivinglab.com </p>


        <p>It works as a QR code-based feedback for  """ + str(name) + """ from anywhere.  </p>
        <p>  </p><br>


    <p>Want to discuss or need a meeting; fix here https://l.ead.me/eventexhibitor</p>



        <p>Thanks again from UX Living Lab, we innovate from people's minds</p>
        <p> Best wishes for """ + str(name) + """  in event</p>


        <p>  </p><br>
        <p> Regards</p>



        <p>""" + str(agent) + """ </p>
        <p>@uxlivinglab</p>
        <p><a href="www.uxlivinglab.com">www.uxlivinglab.com</a></p>
        <img class="one" src="cid:image2"width="100" height="100">

        <p>Note - This mail is specifically sent to """ + str(name) + """ <company name> from uxlivinglab to introduce business. Its not a spam.</p>
        <p>""" + str(client_id) + """ </p>
        <p>------------------------------------------------------------------------------------------------------------------------------------</p>
    </body>
    </html>
    """
    file_name = 'mailernew.gif'
    image_path = os.path.join(script_directory, file_name)
    img = open(image_path, 'rb').read()
    msgImg = MIMEImage(img, 'jpg')
    msgImg.add_header('Content-ID', '<image1>')
    msgImg.add_header('Content-Disposition', 'inline', filename='flyer')
    file_name = 'dowellqr.png'
    image_path = os.path.join(script_directory, file_name)
    img2 = open(image_path, 'rb').read()
    msgImg2 = MIMEImage(img2, 'jpg')
    msgImg2.add_header('Content-ID', '<image2>')
    msgImg2.add_header('Content-Disposition', 'inline', filename='dowellqr3')

    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")
    newMessage.attach(part1)
    newMessage.attach(part2)
    newMessage.attach(msgImg)
    newMessage.attach(msgImg2)

    # fileToSend = os.path.dirname(os.path.abspath(__file__))+'/bdqr.png'
    fileToSend = os.path.dirname(os.path.abspath(__file__)) + '/' + bdqr_name
    ctype, encoding = mimetypes.guess_type(fileToSend)
    if ctype is None or encoding is not None:
        ctype = "application/octet-stream"

    maintype, subtype = ctype.split("/", 1)

    with open(fileToSend, 'rb') as f:
        # set attachment mime and file name, the image type is png
        attachment = MIMEImage(f.read(), _subtype=subtype)
        attachment.add_header("Content-Disposition", "attachment", filename=fileToSend)
        newMessage.attach(attachment)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(Sender_Email, Password)
        smtp.send_message(newMessage)

    client = pymongo.MongoClient(
        "mongodb+srv://qruser:qr_12345@cluster0.n2ih9.mongodb.net/BD_IMAGE?retryWrites=true&w=majority")
    database = client.BD_IMAGE

    fs = gridfs.GridFS(database)

    # Now is all conditions/Exception are fales, then proceed in creating the qrcode

    while True:
        New_resultid = choice(range(1000000000))
        myquery = {'resultid': New_resultid}
        mydoc = database.fs.files.find(myquery)
        db_find_box = []
        for x in mydoc: db_find_box.append(x)
        if len(db_find_box) == 0: break

    # fileName = 'bdqr.png' #The generated qrcode file name
    fileName = bdqr_name  # The generated qrcode file name
    # fileLocation = File_dir_media #The location where the generated qrcode file name is created
    image_path = os.path.join(script_directory, fileName)
    with open(image_path, 'rb') as f:
        contents = f.read()
    # Now store/put the image via GridFs object.
    fileid = fs.put(contents, filename=fileName, encoding='utf-8')
    # Inserting the extra keys and object

    database.fs.files.update_many({'_id': fileid},
                                  {'$set': {"email": form["email"],
                                            "name": form["name"],
                                            "brand_name": form["brand_name"],
                                            "name_incharge": form["name_incharge"],
                                            "designation_incharge": form["designation_incharge"],
                                            "exhibitor_page_link": form["exhibitor_page_link"],
                                            "exhibitor_website": form["exhibitor_website"],
                                            "exhibitor_email": form["exhibitor_email"],
                                            "exhibitor_both_number": form["exhibitor_both_number"],
                                            "exhibitor_city": form["exhibitor_city"],
                                            "exhibitor_country": form["exhibitor_country"],
                                            "exhibitor_address": form["exhibitor_address"],
                                            "type": form["type"],
                                            "exhibitor_product": form["exhibitor_product"],
                                            "linkedin": form["linkedin"],
                                            "twitter": form["twitter"],
                                            "facebook": form["facebook"],
                                            "instagram": form["instagram"],
                                            "youtube": form["youtube"],
                                            "tiktok": form["tiktok"],
                                            "hashtag": form["hashtag"],
                                            "mention": form["mention"],
                                            "description": form["description"],
                                            "comments": form["comments"],
                                            "BDEventID": form["BDEventID"],
                                            "url_generated": generated_url,
                                            }})
    # return {"status":"success", "message":result}
    # os.remove(os.path.dirname(os.path.abspath(__file__))+'/bdqr.png')
    os.remove(os.path.dirname(os.path.abspath(__file__)) + '/' + bdqr_name)
