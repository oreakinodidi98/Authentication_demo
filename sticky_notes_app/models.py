from django.db import models

# Create your models here.
class Stick_notes(models.Model):
    title=models.CharField(max_length=255)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    # foreighn key for author
    author=models.ForeignKey('Author',on_delete=models.CASCADE, null=True , blank=True) # on_delete=models.CASCADE means if author is deleted then all the notes of that author will be deleted

class Author(models.Model):
    name=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    email=models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name

