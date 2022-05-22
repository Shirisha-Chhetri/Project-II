from .models import Genre
from django.contrib.auth.models import User
from django import forms

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre 
        fields = ['title']

#csv file upload garne
class UploadForm(forms.Form):
    uploadfile = forms.FileField()

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password']