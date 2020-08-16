from django.db import models
from addbooks.models import Books
from django.contrib.auth.models import User


# Create your models here.

class Orders(models.Model):
    books = models.ForeignKey(Books, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Order for {self.books.title} placed at {self.date_time} by {self.user.username}'
