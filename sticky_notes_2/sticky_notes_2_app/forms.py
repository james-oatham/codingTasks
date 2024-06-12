from django import forms
from .models import Note


class NoteForm(forms.ModelForm):
    """
    Form for creating and updating note objects.

    Meta class: Defines the model to use (Note) and the fields to
    include in the form.
    """
    class Meta:
        model = Note
        fields = ['title', 'content', 'author', 'colour']
