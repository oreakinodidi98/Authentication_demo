from django.shortcuts import render, redirect, get_object_or_404
from .models import Stick_notes
from .forms import Stick_notesForm
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
    """
    Renders the home page with a list of sticky notes.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - A rendered HTML template with the home page.

    """
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
def notes_create(request):
    """
    View function for creating notes.

    This view function allows authenticated users to create notes. If the request method is POST,
    the data is saved to the database. If the form is valid, the note is saved and the user is
    redirected to the home page. If the request method is GET, a new form object is created.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - If the request method is POST and the form is valid, redirects to the home page.
    - If the request method is GET, renders the 'notes_form.html' template with the note form.

    """
    if request.method == "POST":
        note_form = Stick_notesForm(request.POST)
        if note_form.is_valid():
            note = note_form.save(commit=False)
            note.save()
            return redirect('home') 
    else:
        note_form = Stick_notesForm()
    return render(request, 'notes_form.html', {'note_form': note_form})


# views for details of specific notes
def notes_detail(request, pk):
    """
    View function to display the details of a note.

    Args:
        request (HttpRequest): The HTTP request object.
        pk (int): The primary key of the note.

    Returns:
        HttpResponse: The HTTP response object containing the rendered template.
    """
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
def notes_update(request, pk):
    """
    View function for updating notes.

    Args:
        request (HttpRequest): The HTTP request object.
        pk (int): The primary key of the note to be updated.

    Returns:
        HttpResponse: The HTTP response object.

    Raises:
        Http404: If the note with the given primary key does not exist.
    """
    # get the notes object
    note = get_object_or_404(Stick_notes, pk=pk)
    
    if request.method == "POST":
        # form object
        note_form = Stick_notesForm(request.POST, instance=note)
        
        if note_form.is_valid():
            # save the data to database
            note = note_form.save(commit=False)
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
    



