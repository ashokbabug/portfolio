from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from .forms import ContactMeForm
from django.contrib import messages


# Create your views here.


def Home(request):
    form = ContactMeForm()
    if request.method == "POST":
        form = ContactMeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, f"Your response has been recorded.You will get an email soon"
            )
            return redirect("success")
    else:
        form = ContactMeForm()

    context = {"form": form}
    return render(request, "myprofile/index.html", context)


def Success(request):
    return render(request, "myprofile/success.html")
