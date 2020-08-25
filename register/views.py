from django.shortcuts import render, redirect
from .forms import NewUser
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login


# Create your views here.
@csrf_protect
def register(response):
    if response.method == "POST":
        form = NewUser(response.POST)
        if form.is_valid():

            form.save()
            return redirect('/')

    else:
        form = NewUser()
    return render(response, "register/register.html", {"form": form})
