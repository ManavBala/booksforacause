from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=20)
    book_img = models.ImageField(null=True, blank=True)
    book_auth = models.CharField(max_length=300)
    book_pub = models.CharField(max_length=300)
    book_cond = models.CharField(max_length=1)
    book_user = models.ForeignKey(User, on_delete=models.CASCADE)
    book_price = models.IntegerField()
    approved = models.IntegerField(default=0)

    def __str__(self):
        return self.title
