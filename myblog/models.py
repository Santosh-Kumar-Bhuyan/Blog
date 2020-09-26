from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.EmailField()
    msg = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name

class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=220)
    author = models.CharField(max_length=25)
    slug = models.CharField(max_length=200)
    content = models.TextField()
    timestamp = models.DateTimeField(blank=True)
    image = models.ImageField(upload_to="static/img" , default="")

    def __str__(self):
        return self.title + ' by ' + self.author