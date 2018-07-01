from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
User = get_user_model()

class SignUpForm(UserCreationForm):
    phone_number = forms.CharField(max_length=16, required=True)
    class Meta:
        model = User
        fields = ('phone_number', 'password1', 'password2')
