from django.test import TestCase, Client
# import reverse
from django.urls import reverse
# import models from sticky_notes_app
from sticky_notes_app.models import Stick_notes
#import forms from auth_app
from auth_app.forms import RegisterForm
# import User and Group from django.contrib.auth.models
from django.contrib.auth.models import User, Group
# import login and logout from django.contrib.auth
from django.contrib.auth import login, logout

# Create your tests here.

# test for posting a note
class TestPostNotes(TestCase):
    # create a set up method to run before each test
    def setUp(self):
        # create a test_author object for testing
        #test_author = Author.objects.create(name=' testingdemo', username='Test1Username', email='Test@gmail.com', password='Password', date_of_birth='2021-01-01')
        # create a Stick_notes object for testing
        Stick_notes.objects.create(title='Test Title', content='Test Content', author= test_author)
        
        

    # create a method test_notes_has title to test if the title is correct
    def test_notes_has_title(self):
        # get the Stick_notes object
        note = Stick_notes.objects.get(title='Test Title')
        # assert if the title is correct
        self.assertEqual(note.title, 'Test Title')

    # create a method test_notes_has_content to test if the content is correct
    def test_notes_has_content(self):
        # get the Stick_notes object
        note = Stick_notes.objects.get(content='Test Content')
        # assert if the content is correct
        self.assertEqual(note.content, 'Test Content')
        
# class for testing the views
class TestViews(TestCase):
    # create a set up method to run before each test
    def setUp(self):
        # create a author object for testing
        #test_author = Author.objects.create(name=' testingdemo', username='Test1Username', email='Test@gmail.com', password='Password', date_of_birth='2021-01-01')
        # create a Stick_notes object for testing
        Stick_notes.objects.create(title='Test Title2', content='Test Content 2', author= test_author)
        # # django test client
        # self.client = Client()
        # #login the user 
        # self.client.login(username='tom', password='password')
        # # create a RegisterForm object for testing
        # form = RegisterForm(data={'username': 'Test2Username', 'email': 'test@gmail.com', 'password': 'Password', 'password_conf': 'Password'})
        # # create a User object for testing
        # new_user = User()
        # # set the username and password
        # new_user.username = form.cleaned_data['username']
        # new_user.set_password(form.cleaned_data['password'])
        # new_user.save()
        # # add user to poster group
        # group = Group.objects.get(name='Posters')
        # new_user.groups.add(group)
        # # login the user
        # login(request, new_user)

    # create a method test_home_view to test the home view
    def test_home_view(self):
        # get the response from the home view and follow the redirect
        response = self.client.get(reverse('home'), follow=True)
        # assert if the status code is 200, as we're following the redirect
        self.assertEqual(response.status_code, 200)
        # assert if the template used is home.html
        self.assertTemplateUsed(response, 'registration/login.html')
    
    # create a method test_notes_detail_view to test the notes_detail view
    def test_notes_detail_view(self):
        # notes object getting pk
        note = Stick_notes.objects.get(pk=1)
        # get the response from the notes_detail view
        response = self.client.get(reverse('notes_detail', args=[note.pk]))
        # assert if the status code is 200
        self.assertEqual(response.status_code, 200)
        # assert if the template used is notes_form.html
        self.assertTemplateUsed(response, 'notes_detail.html')
        # assert if the responce contains the note title
        self.assertContains(response, 'Test Title2')
