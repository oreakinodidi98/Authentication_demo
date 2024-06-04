from django.db import models

# Create your models here.

"""
    A model representing a sticky note.

    Attributes:
        title (str): The title of the sticky note.
        content (str): The content of the sticky note.
        created_at (datetime): The date and time when the sticky note was created.
    """
class Stick_notes(models.Model):
    title=models.CharField(max_length=255)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title

