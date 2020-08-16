from django.shortcuts import render
from .models import Orders
from django.contrib.auth.models import User
from addbooks.models import Books
from datetime import datetime
import pytz


# Create your views here.
def place_order(response, book_id):

    book = Books.objects.get(pk=book_id)
    new_order = Orders(books=book, user=response.user)
    new_order.save()
    return render(response, "orders/place_order.html")
