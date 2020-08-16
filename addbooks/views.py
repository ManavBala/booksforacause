from django.shortcuts import render, redirect
from .forms import BookForm
from django.views.decorators.csrf import csrf_protect


# Create your views here.
@csrf_protect
def addbooks(request):
    form = BookForm()
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)

        if form.is_valid():
            form.instance.book_user = request.user
            form.save()

            return redirect("/")
    else:
        form = BookForm()
    return render(request, "addbooks/addbook.html", {"form": form})
