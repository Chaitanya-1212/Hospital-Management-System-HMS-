from django.core.mail import EmailMessage
from django.template.loader import render_to_string

def appoinment_email(email,apot):
    subject="Appointment Booked"
    body=render_to_string("mail.html",{"apot":apot})
    mail=EmailMessage(subject,body,to=[email,])
    mail.content_subtype="html"
    mail.send()