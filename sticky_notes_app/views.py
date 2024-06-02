from django.shortcuts import render, redirect, get_object_or_404
from .models import Stick_notes, Author
from .forms import Stick_notesForm, UserRegisterForm
# import authentication form from django
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
# import login required
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

# can also add login required decorator to restrict access to authenticated users only 
@login_required
def home(request):
    notes = Stick_notes.objects.all()
    # context dictionary to pass data to template
    context = {
        'notes': notes,
        'page_title': 'Home Page'
               }
    return render(request, 'home.html', context)
# views for CRUD functionality

# add permission required decorator to restrict access to authenticated users only
# add name of app and model to permission_required decorator, model in this case is Stick_notes so lower case and separated by underscore
@permission_required('sticky_notes_app.add_stick_notes', login_url='login')
# view for creating notes
def notes_create(request):
    # if user is authenticated, they can proceed to create notes
    # if request is post then save the data
    if request.method == "POST":
        # form object
        note_form = Stick_notesForm(request.POST)
        # if form is valid then save the data
        if note_form.is_valid():
            # save the data to database
            note= note_form.save(commit=False)
            # if user is authenticated then set the author
            if request.user.is_authenticated:
                # set the author
                note.author = request.user
                # save the data
            note.save()
            # redirect to home page
            return redirect('home') 
    else:
        # if request is get then create the form object
        note_form = Stick_notesForm()
    return render(request, 'notes_form.html', {'note_form': note_form})


# views for details of specific notes
def notes_detail(request, pk):
    # get the notes object
    note = get_object_or_404(Stick_notes, pk=pk)
    # context dictionary to pass data to template
    context = {
        'note': note
    }
    return render(request, 'notes_detail.html', context)

# add permission required decorator to restrict access to authenticated users only
# add name of app and model to permission_required decorator, model in this case is Stick_notes so lower case and separated by underscore
@permission_required('sticky_notes_app.change_stick_notes', login_url='home')
# view for updating notes
def notes_update(request, pk):
    # get the notes object
    note = get_object_or_404(Stick_notes, pk=pk)
    # if request is post then save the data
    if request.method == "POST":
        # form object
        note_form = Stick_notesForm(request.POST, instance=note)
        # if form is valid then save the data
        if note_form.is_valid():
            # save the data to database
            note = note_form.save(commit=False)
            # if user is authenticated then set the author
            if request.user.is_authenticated:
                # set the author
                note.author = request.user
                # save the data
            note.save()
            # redirect to home page
            return redirect('home') 
    else:
        # if request is get then create the form object
        note_form = Stick_notesForm(instance=note)
    return render(request, 'notes_form.html', {'note_form': note_form})

# add permission required decorator to restrict access to authenticated users only

@permission_required('sticky_notes_app.delete_stick_notes', login_url='home')
# view for deleting notes
def notes_delete(request, pk):
    # get the notes object
    note = get_object_or_404(Stick_notes, pk=pk)
    # delete the data
    note.delete()
    # redirect to home page
    return redirect('home')
    
# # view for signing in user
# def author_create(request):
#     # if request is post then save the data
#     if request.method == "POST":
#         # form object
#         author_form  = AuthenticationForm(request, data=request.POST)
#         # if form is valid then save the data
#         if author_form.is_valid():
#             # get the username and password
#             username = author_form.cleaned_data.get('username')
#             password = author_form.cleaned_data.get('password')
#             # authenticate the user
#             user = authenticate(username=username, password=password)
#             # if user is not None then login the user
#             if user is not None:
#                 # login the user
#                 login(request, user)
#                 # display message
#                 messages.success(request, f'Welcome {username}!')
#                 # redirect to home page
#                 return redirect('home')
#             else:
#                 # display message
#                 messages.error(request, 'Invalid username or password.')  
#         else:
#             # display message
#             messages.error(request, 'Invalid username or password.')
#     author_form = AuthenticationForm()
#     # context dictionary to pass data to template
#     context = {
#         'page_title': 'Login Page',
#         'author_form': author_form
#                }
#     return render(request, 'login.html', context)

# # view for registering user
# def author_register(request):
#     # if request is post then save the data
#     if request.method == "POST":
#         # form object
#         author_form = UserRegisterForm(request.POST)
#         # if form is valid then save the data
#         if author_form.is_valid():
#             # save the data to database
#             author_form.save()
#             # get username
#             username = author_form.cleaned_data.get('username')
#             # display message
#             messages.success(request, f'Account created for {username}!')
#             # redirect to login page
#             return redirect('author_create') 
#     else:
#         # if request is get then create the form object
#         author_form = UserRegisterForm()
#     # context dictionary to pass data to template
#     context = {
#         'page_title': 'Login Page',
#         'author_form': author_form
#                }
#     return render(request, 'register.html', context)

# # view for signing out user
# def author_logout(request):
#     # logout the user
#     logout(request)
#     # display message
#     messages.info(request, 'You have successfully logged out.')
#     # redirect to home page
#     return redirect('home')


