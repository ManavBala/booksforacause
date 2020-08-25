from django.shortcuts import render, redirect

from addbooks.models import Books

from .models import Orders

from django.core.mail import send_mail
from website.settings import EMAIL_HOST_USER
from django.views.decorators.csrf import csrf_protect


# Create your views here.
def place_order(response, book_id):
    book = Books.objects.get(pk=book_id)
    new_order = Orders(books=book, user=response.user)
    new_order.save()
    send_mail('Test', "test", EMAIL_HOST_USER, ["manav.gipsy23@gmail.com"])

    return render(response, "orders/place_order.html")


def my_orders(response):
    posts = Orders.objects.filter(user=response.user)
    delete_id = response.GET.get("delete")
    if delete_id:
        Orders.objects.get(pk=delete_id).delete()

    return render(response, "orders/my_orders.html", {"posts": posts})


def order_page(response, id):
    posts = Orders.objects.get(pk=id)

    return render(response, "orders/order_page.html", {"posts": posts})
@csrf_protect
def order_cancel(response, id):
    posts = Orders.objects.get(pk=id)
    order_name = posts.books.title
    order_date = posts.date_time
    posts.delete()

    return redirect("/my_orders")

def order_recieved(response, id):
    posts = Orders.objects.get(pk=id)
    posts.delete()

    return redirect("/my_orders")