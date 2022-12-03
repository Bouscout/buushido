from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class formulaire_incription(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields =('username',)
   
class formulaire_connection(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
