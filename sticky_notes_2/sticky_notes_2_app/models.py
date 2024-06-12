from django.db import models


# Create your models here.
class Note(models.Model):
    """
    Model representing a sticky note.

    ForeignKey relationships representing the author and colour of the post.
    No specific methods are defined in this model.
    """
    # Main attributes for Notes class.
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    # Related attributes (Foreign Keys).
    author = models.ForeignKey('Author', on_delete=models.CASCADE,
                               null=True, blank=True)

    colour = models.ForeignKey('Colour', on_delete=models.CASCADE,
                               null=True, blank=True)

    def __str__(self):
        return self.title


class Author(models.Model):
    """ Model representing the author of a sticky note. """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Colour(models.Model):
    """ Model representing the background colour of a sticky note. """
    colour_name = models.CharField(max_length=255)

    def __str__(self):
        return self.colour_name
