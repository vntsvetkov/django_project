from django.db import models


class HashTag(models.Model):

    name = models.CharField(max_length=120, null=False)

class Author(models.Model):

    name = models.CharField(max_length=120, null=False)

# Create your models here.
class Post(models.Model):

    image = models.ImageField(upload_to='images/', null=True)
    title = models.CharField(max_length=120, null=False)
    text = models.TextField(null=False)
    author = models.CharField(max_length=50)
    publish_date = models.DateField(null=False)

    objects = models.Manager()

    def __str__(self):
        return self.title
