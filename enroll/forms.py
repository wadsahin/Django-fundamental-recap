from django import forms
from .models import userModel

class userForm(forms.Form):
    username = forms.CharField(max_length=70)
    firstname = forms.CharField(max_length=70)
    lastname = forms.CharField(max_length=70)
    email = forms.EmailField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())
    re_password = forms.CharField(widget=forms.PasswordInput())

class modelForm(forms.ModelForm):
    class Meta:
        model = userModel
        fields = '__all__'
        labels = {'email': 'Enter your Email'}

