from django.shortcuts import render
from addbooks.models import Books
# Create your views here.
def dev(response):
    posts= Books.objects.all().filter(approved=0)

    return render(response, "dev/dev.html", {"posts": posts})