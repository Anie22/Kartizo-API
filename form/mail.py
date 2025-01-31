from django.conf import settings
from django.core.mail import EmailMessage


def send_success_mail(email, consulting_booked):
    Subject = 'Order Request - Kartizo Global'
    email_body = f'Hi {consulting_booked['fullName']} your order request has been made. Our team will contact you with futher information'
    from_email = settings.DEFAULT_FROM_EMAIL

    email = EmailMessage(subject=Subject, body=email_body, from_email=from_email, to=[email])
    email.send()

def send_admin_mail(consulting_booked):
    subject = 'New Appointment Booked'
    body = f"A new appointment has been booked by a customer(client)\n{consulting_booked['fullName']}\n{consulting_booked['email']}\n{consulting_booked['phoneNumber']}\n{consulting_booked['service']}\n{consulting_booked['date']}\n{consulting_booked['time']}\n{consulting_booked['address']}\n{consulting_booked['message']}"
    from_email = settings.DEFAULT_FROM_EMAIL
    to_email = settings.EMAIL_HOST_USER

    email = EmailMessage(subject=subject, body=body, from_email=from_email, to=[to_email])
    email.send()