# import unittest
import unittest
# intort views from sticky_notes_app
from sticky_notes_app import notes_create, notes_detail, notes_update, notes_delete
# import Stick_notesForm from sticky_notes_app
from sticky_notes_app.forms import Stick_notesForm

# create a class TestViews
class TestViews(unittest.TestCase):
    # create a set up method to run before each test
    def setUp(self):
        # create a note_form object from my .form file using Stick_notesForm and fill it out
        self.note_form = Stick_notesForm(data={
            'title': 'Test Title',
            'content': 'Test Content',
            'author': 'Test Author',
        })

    # create a method test_notes_create
    def test_notes_create(self):
        # arrange - create a note_form object
        note_form = Stick_notesForm()
        # act - call notes_create with 'POST' and 'GET'
        result = notes_create('POST') 
        result2 = notes_create('GET')
        # assert - check if the result is equal to 'home' and 'notes_form.html'
        self.assertEqual(result, 'home')
        self.assertEqual(result2, 'notes_form.html')
        


    def test_notes_detail(self):
        # Arrange
        note_id = 1
        note = Stick_notesForm.create(id=note_id, title='Test Title', content='Test Content', author='Test Author')
        # Act
        result = notes_detail(note_id)
        # Assert
        self.assertEqual(result, note)
        #self.assertEqual(notes_detail(1), 'notes_detail.html')

    def test_notes_update(self):
        self.assertEqual(notes_update('POST', 1), 'home')
        self.assertEqual(notes_update('GET', 1), 'notes_form.html')

    def test_notes_delete(self):
        self.assertEqual(notes_delete(1), 'notes_delete.html')

