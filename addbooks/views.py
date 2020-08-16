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
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()

            return redirect("/")
    else:
        form = BookForm()
    return render(request, "addbooks/addbook.html", {"form": form})
