from django.urls import path
from .views import (note_list, note_list_by_author, note_list_by_colour,
                    note_detail, note_create, note_update, note_delete)

urlpatterns = [
    # URL pattern for displaying a list of all notes.
    path('', note_list, name='note_list'),

    # URL pattern for displaying a list of notes by author.
    path('who/<str:author>/', note_list_by_author, name='note_list_by_author'),

    # URL pattern for displaying a list of notes by colour.
    path('col/<str:colour>/', note_list_by_colour, name='note_list_by_colour'),

    # URL pattern for displaying details of a specific note.
    path('note/<int:pk>/', note_detail, name='note_detail'),

    # URL pattern for creating a new note.
    path('note/new/', note_create, name='note_create'),

    # URL pattern for updating an existing note.
    path('note/<int:pk>/update/', note_update, name='note_update'),

    # URL pattern for deleting an existing note.
    path('note/<int:pk>/delete/', note_delete, name='note_delete'),
]
