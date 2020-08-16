from django.shortcuts import render
from addbooks.models import Books
from django.http import HttpResponse
from .forms import ContactDeveloper
from django.core.paginator import Paginator


# Create your views here.
def home(request):
    posts = Books.objects.all()
    query = request.GET.get("q")
    if query:
        posts = posts.filter(title__icontains=query)

    paginator = Paginator(posts, per_page=25)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1

    try:
        posts = paginator.page(page)
    except:
        posts = paginator.page(paginator.num_pages)
    return render(request, "Home/home.html", {"posts": posts})


def view_books(request, id):
    posts = Books.objects.get(pk=id)

    return render(request, "Home/book_page.html", {"posts": posts})


def contact_dev(response):
    form = ContactDeveloper()
    return render(response, "Home/forms.html", {"form": form})
