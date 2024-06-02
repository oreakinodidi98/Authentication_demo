from django import forms
from .models import Stick_notes
# use default user creation form from django
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# form for creating notes
class Stick_notesForm(forms.ModelForm):
    class Meta:
        model = Stick_notes
        fields = ('title', 'content', 'author')

# form for registering user
class UserRegisterForm(UserCreationForm):

    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'password1': forms.PasswordInput(),
            'password2': forms.PasswordInput()
        }