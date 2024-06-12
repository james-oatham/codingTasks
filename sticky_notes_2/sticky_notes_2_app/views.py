from django.shortcuts import render, get_object_or_404, redirect
from .models import Note, Author, Colour
from .forms import NoteForm


# Create your views here.
def note_list(request):
    """ View to display the list of all notes (unfiltered). """
    notes = Note.objects.all()
    count = Note.objects.count()

    context = {
        'notes': notes,
        'count': count,
        'page_title': 'List of Sticky Notes',
    }

    return render(request, 'notes/note_list.html', context)


def note_list_by_author(request, author):
    """ View to display the list of all notes by an author. """
    author = get_object_or_404(Author, name=author)

    notes_by_author = Note.objects.filter(author=author.id)
    count_by_author = Note.objects.filter(author=author.id).count()

    context = {
        'author_name': author.name,
        'notes_by_author': notes_by_author,
        'count_by_author': count_by_author,
        'page_title': 'List of Sticky Notes by Author',
    }

    return render(request, 'notes/note_list_by_author.html', context)


def note_list_by_colour(request, colour):
    """ View to display the list of all notes by a colour. """
    colour = get_object_or_404(Colour, colour_name=colour)

    notes_by_colour = Note.objects.filter(colour=colour.id)
    count_by_colour = Note.objects.filter(colour=colour.id).count()

    context = {
        'colour_name': colour.colour_name,
        'notes_by_colour': notes_by_colour,
        'count_by_colour': count_by_colour,
        'page_title': 'List of Sticky Notes by Colour',
    }

    return render(request, 'notes/note_list_by_colour.html', context)


def note_detail(request, pk):
    """ View to display the details of a specific note. """
    note = get_object_or_404(Note, pk=pk)
    return render(request, 'notes/note_detail.html', {'note': note})


def note_create(request):
    """ View to create a new note. """
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            if request.user.is_authenticated:
                note.author = request.user
            note.save()
        return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'notes/note_form.html', {'form': form})


def note_update(request, pk):
    """ View to update an existing note. """
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save(commit=False)
            note.save()
            return redirect('note_list')
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/note_form.html', {'form': form})


def note_delete(request, pk):
    """ View to delete an existing note. """
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return redirect('note_list')
