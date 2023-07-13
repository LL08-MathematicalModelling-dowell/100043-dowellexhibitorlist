import os
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from random import randint

from django.conf import settings
from pymongo import MongoClient

from .models import MailCount


# define the scope
def mail(form):
    # getting count to how many emails have done
    email_count = MailCount.objects.filter(pk=1)
    print(email_count[0].count)
    updated_count = email_count[0].count + 10
    print(updated_count)
    MailCount.objects.filter(pk=1).update(count=updated_count)

    client_id = randint(100000000000000000000000, 999999999999999999999999)
    client_id = str(client_id)
    brand = form['brand_name']
    name = form['brand_name']
    exhibitor_email = form["exhibitor_email"]
    agent = "Netal Pareek"
    linkedin = form["linkedin"]
    twitter = form["twitter"]
    website = form["exhibitor_website"]

    # if form["name_incharge"] == "NA" or form["name_incharge"] == "na" or form["name_incharge"] == "Na":
    #     detail = "Hi"
    # else:
    #     detail = "Hi "+form["name_incharge"]
    detail = "Hi"

    Sender_Email = "uxlivinglab@dowellresearch.uk"
    Reciever_Email = exhibitor_email
    Password = "bkefonjnfuohhhyc"

    newMessage = MIMEMultipart()
    newMessage['Subject'] = "UX/UI Design trends for " + str(
        name) + " from UX Living Lab News on Linkedin, inviting you to Subscribe"

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

    <p>Are you a UX/UI enthusiast? Subscribe <a href="https://l.ead.me/UxlivinglabNews">here</a>
        to this weekly newsletter on Linkedin from DoWell UX Living Lab</p>

    <a href="https://l.ead.me/UxlivinglabNews"><img class="one" src="cid:image1"width="640" height="360"></a>
        <p>This weekly newsletter talks globally about</p>
        <br>
        <ul>
            <li>UX/UI trends</li>
            <li>UX/UI project strategies</li>
            <li>UX Research methodologies</li>
            <li>How to execute UX/UI projects</li>
            <li>Success/failure stories in UX/UI</li>
            <li>UX/UI designer as a profession</li>
            <li>Important events in UX/UI</li>
        </ul>
        <br>
        <p>Subscribe <a href="https://l.ead.me/UxlivinglabNews">https://l.ead.me/UxlivinglabNews</a> and get updated</p>
        <p>Want to discuss or need a meeting with uxlivinglab? <a href="https://l.ead.me/eventexhibitor">Fix here</a></p>
        <p>Thanks again from UX Living Lab, we innovate from people's minds</p>
        <br>
        <p>Thank you</p>
        <p>""" + str(agent) + """ </p>
        <p>@uxlivinglab</p>
        <p><a href="www.uxlivinglab.com">www.uxlivinglab.com</a></p>
        <img class="one" src="cid:image2"width="100" height="100">

        <p>Note - This mail is specifically sent to """ + str(name) + """ from uxlivinglab to introduce business. Its not a spam.</p>
        <p>------------------------------------------------------------------------------------------------------------------------------------</p>
    </body>
    </html>
    """
    file_name = 'new_mail_image.png'
    script_directory = os.path.dirname(os.path.abspath(__file__))
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
    msgImg2.add_header('Content-Disposition', 'inline', filename='dowellqr')

    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")
    newMessage.attach(part1)
    newMessage.attach(part2)
    newMessage.attach(msgImg)
    newMessage.attach(msgImg2)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(Sender_Email, Password)
        smtp.send_message(newMessage)

    # getting 10 email address from the database and sending them mail
    string = settings.MONGODB_CONN
    connection = MongoClient(string)
    db = connection['exhibitor_details']
    collection = db['fs.files']
    for doc in collection.find({}).skip(email_count[0].count).limit(10):
        # print(doc)
        client_id = randint(100000000000000000000000, 999999999999999999999999)
        client_id = str(client_id)
        if "exhibitor_email" in doc:
            name = doc['brand_name']
            exhibitor_email = doc["exhibitor_email"]
            print(exhibitor_email)
            detail = "Hi"

            Sender_Email = "uxlivinglab@dowellresearch.uk"
            Reciever_Email = exhibitor_email
            Password = "bkefonjnfuohhhyc"

            newMessage = MIMEMultipart()
            newMessage['Subject'] = "UX/UI Design trends for " + str(
                name) + " from UX Living Lab News on Linkedin, inviting you to Subscribe"

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

            <p>Are you a UX/UI enthusiast? Subscribe <a href="https://l.ead.me/UxlivinglabNews">here</a>
                to this weekly newsletter on Linkedin from DoWell UX Living Lab</p>

            <a href="https://l.ead.me/UxlivinglabNews"><img class="one" src="cid:image1"width="640" height="360"></a>
                <p>This weekly newsletter talks globally about</p>
                <br>
                <ul>
                    <li>UX/UI trends</li>
                    <li>UX/UI project strategies</li>
                    <li>UX Research methodologies</li>
                    <li>How to execute UX/UI projects</li>
                    <li>Success/failure stories in UX/UI</li>
                    <li>UX/UI designer as a profession</li>
                    <li>Important events in UX/UI</li>
                </ul>
                <br>
                <p>Subscribe <a href="https://l.ead.me/UxlivinglabNews">https://l.ead.me/UxlivinglabNews</a> and get updated</p>
                <p>Want to discuss or need a meeting with uxlivinglab? <a href="https://l.ead.me/eventexhibitor">Fix here</a></p>
                <p>Thanks again from UX Living Lab, we innovate from people's minds</p>
                <br>
                <p>Thank you</p>
                <p>""" + str(agent) + """ </p>
                <p>@uxlivinglab</p>
                <p><a href="www.uxlivinglab.com">www.uxlivinglab.com</a></p>
                <img class="one" src="cid:image2"width="100" height="100">

                <p>Note - This mail is specifically sent to """ + str(name) + """ from uxlivinglab to introduce business. Its not a spam.</p>
                <p>------------------------------------------------------------------------------------------------------------------------------------</p>
            </body>
            </html>
            """
            file_name = 'new_mail_image.png'
            script_directory = os.path.dirname(os.path.abspath(__file__))
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
            msgImg2.add_header('Content-Disposition', 'inline', filename='dowellqr')

            part1 = MIMEText(text, "plain")
            part2 = MIMEText(html, "html")
            newMessage.attach(part1)
            newMessage.attach(part2)
            newMessage.attach(msgImg)
            newMessage.attach(msgImg2)

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(Sender_Email, Password)
                smtp.send_message(newMessage)
