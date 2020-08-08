from django.contrib import admin
from .models import ContactMe

# Register your models here.
class ContactMeAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "number",
        "place",
        "time",
    )
    list_filter = ("completed",)
    search_fields = ("name",)
    order_by = "-time"


admin.site.register(ContactMe, ContactMeAdmin)
