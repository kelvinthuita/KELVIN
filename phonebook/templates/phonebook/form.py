from django contrib.auth.models import User
from django import forms
class UserForm(forms.modelForm):
    password= "forms.charField"(widget=forms.PassswordInput)

    Class Meta:
    model = User
    field = ["username", 'email', "password"]