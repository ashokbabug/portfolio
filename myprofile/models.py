from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
from phonenumber_field.modelfields import PhoneNumberField
from portfolio.settings import EMAIL_HOST_USER

from django.core.mail import BadHeaderError, send_mail
from django.template.loader import render_to_string
from django.core.mail import mail_admins


class ContactMe(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField()
    number = models.BigIntegerField()
    place = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=1000)
    accepted = models.BooleanField(default=False, blank=True, null=True)
    completed = models.BooleanField(default=False, blank=True, null=True)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "ContactMe"
        verbose_name_plural = "ContactMe"


@receiver(post_save, sender=ContactMe)
def create_ContactMe(sender, instance, created, **kwargs):
    if created:
        message = render_to_string(
            "myprofile/send_email_admin.html",
            {
                "name": instance.name,
                "email": instance.email,
                "mobile_number": instance.number,
                "place": instance.place,
            },
        )
        mail_subject = "Thanks For Contacting Me"
        to_mail = instance.email
        send_mail(
            mail_subject,
            f"We have recieved your request.We will let you soon and discuss about the project",
            EMAIL_HOST_USER,
            [to_mail],
            fail_silently=True,
        )
        send_mail(
            "Hello,Sir You got a new project",
            message,
            EMAIL_HOST_USER,
            ["gashokbabu999@gmail.com"],
            fail_silently=True,
        )
