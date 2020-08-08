from django.forms import ModelForm
from .models import ContactMe


class ContactMeForm(ModelForm):
    class Meta:
        model = ContactMe
        fields = ["name", "email", "number", "place", "subject", "message"]
