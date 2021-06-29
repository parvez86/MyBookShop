from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *


# Create your forms here.
class Product(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["img", "name", "price", "desc", "url"]


#
class NewUserForm(UserCreationForm):
    email = forms.EmailField(max_length=50, required=True)
    username = forms.CharField(max_length=30, required=True)
    password = forms.CharField(required=True, max_length=50)
    first_name = forms.CharField(max_length=30, required=True)

    class Meta:
	    model = User
	    fields = ("username", "email", "password", "first_name", "last_name")


    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['username']
        user.password = self.cleaned_data['password']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user