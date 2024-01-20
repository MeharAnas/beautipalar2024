# views.py

from django.shortcuts import render
from .models import Booking
from django.http import HttpResponse
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.contrib import messages


def index(request):
    return render(request, 'beauti.html')

def mail_send(Name, Email, Number, Category, Date, Message):
    import smtplib

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
    # start TLS for security
    s.starttls()
    # Authentication
    s.login("meharanas182@gmail.com", "rapl wzwk hxud yzqw")

    # create a MIMEMultipart object
    msg = MIMEMultipart()
    msg['From'] = "meharanas182@gmail.com"
    msg['To'] = "sufyan7586432@gmail.com"
    msg['Subject'] = "New Reservation: " + Name

    # attach the message to the MIMEMultipart object
    msg.attach(MIMEText(f"Name: {Name}\nEmail: {Email}\nNumber: {Number}\nCategory: {Category}\nDate: {Date}\nMessage: {Message}", 'plain'))

    # sending the mail
    s.sendmail("meharanas182@gmail.com", "meharanas182@gmail.com", msg.as_string())

    # terminating the session
    s.quit()
    print('done')

def saveEnquiry(request):
    if request.method == "POST":
        Name = request.POST.get('name')
        Email = request.POST.get('email_address')
        Number = request.POST.get('phone')
        Category = request.POST.get('category')
        Date = request.POST.get('date')
        Message = request.POST.get('message')

        print(Name, Email, Number, Category, Date, Message)
        mail_send(Name, Email, Number, Category, Date, Message)

        en = Booking(Name=Name, Email=Email, Number=Number, Category=Category, Date=Date, Message=Message)
        en.save()
        print("data saved successfully")

        # messages.success(request,"Data send ")

    return render(request, 'beauti.html')
