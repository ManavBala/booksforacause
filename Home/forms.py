from django import forms


class ContactDeveloper(forms.Form):
    subject = forms.CharField(max_length=200)
    description = forms.CharField(max_length=1000)
