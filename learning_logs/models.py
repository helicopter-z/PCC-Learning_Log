from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Topic(models.Model):
    """A topic the user is learning about"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text


class Entry(models.Model):
    """Something specific learned about a topic"""
    topic = models.ForeignKey(Topic, on_delete=models.DO_NOTHING)  # foreign key: a reference to another record in the database
    text = models.TextField()  # doesn't need a size limit
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'  # without this, Django would refer to multiple entries as 'Entrys'

    def __str__(self):
        """Return a string representation of the model."""
        return self.text[:50] + "..."
