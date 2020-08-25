from django.forms import ModelForm
from .models import Books
from django.views.decorators.csrf import csrf_protect
from django import forms


class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = '__all__'
        exclude = ['book_user', 'approved']

