from django.db import models
from datetime import date


# Create your models here.
class Post(models.Model):

    title = models.CharField(max_length=120, null=False)
    text = models.TextField(null=False)
    author = models.CharField(max_length=20)
    publish_date = models.DateField(null=False, default=date.today())

    objects = models.Manager()

    def __str__(self):
        return self.title