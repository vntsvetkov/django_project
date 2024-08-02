from django.db import models


class HashTag(models.Model):

    name = models.CharField(max_length=120, null=False)

    def __str__(self):
        return self.name


class Author(models.Model):

    name = models.CharField(max_length=120, null=False)

    def __str__(self):
        return self.name


# Create your models here.
class Post(models.Model):

    image = models.ImageField(upload_to='images/', null=True)
    title = models.CharField(max_length=120, null=False)
    text = models.TextField(null=False)
    author = models.ForeignKey(
        'Author',
        on_delete=models.DO_NOTHING
    )
    publish_date = models.DateField(null=False)
    tags = models.ManyToManyField(HashTag)
    objects = models.Manager()

    def __str__(self):
        return self.title
