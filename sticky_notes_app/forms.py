from django import forms
from .models import Stick_notes
# use default user creation form from django
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# form for creating notes

"""
    A form class for creating and updating Stick_notes objects.

    This form is used to handle the creation and updating of Stick_notes objects.
    It is a ModelForm that is automatically generated based on the Stick_notes model.

    Attributes:
        model (class): The Stick_notes model class.
        fields (tuple): The fields to include in the form.

    Example:
        To use this form, simply instantiate it and pass it to the view or template:

        >>> form = Stick_notesForm()
        >>> context = {'form': form}
        >>> return render(request, 'template.html', context)
    """
class Stick_notesForm(forms.ModelForm):

    class Meta:
        model = Stick_notes
        fields = ('title', 'content')

# form for registering user

"""
    A form used for user registration.

    This form extends the UserCreationForm provided by Django to include an email field.
    It allows users to register by providing a username, email, and password.

    Attributes:
        email (forms.EmailField): The email field for the user's email address.

    Meta:
        model (User): The User model to be used for registration.
        fields (tuple): The fields to be included in the form.
        widgets (dict): The widgets to be used for password fields.

    """
class UserRegisterForm(UserCreationForm):

    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'password1': forms.PasswordInput(),
            'password2': forms.PasswordInput()
        }