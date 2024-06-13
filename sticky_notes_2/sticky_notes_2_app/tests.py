from django.test import TestCase
from django.urls import reverse
from sticky_notes_2_app.models import Note, Author, Colour


# Tests for Note objects (create and retrieve).
class NoteModelTest(TestCase):
    def setUp(self):
        # Create an Author object.
        author = Author.objects.create(name='Test Author')

        # Create a Colour object.
        colour = Colour.objects.create(colour_name='yellow')

        # Create a Note object for testing.
        Note.objects.create(title='Test Note',
                            content='This is a test note.',
                            author=author, colour=colour)

    def test_note_has_title(self):
        # Test that a Note object has the expected title.
        note = Note.objects.get(id=1)
        self.assertEqual(note.title, 'Test Note')

    def test_note_has_content(self):
        # Test that a Note object has the expected content.
        note = Note.objects.get(id=1)
        self.assertEqual(note.content, 'This is a test note.')

    def test_note_has_colour(self):
        # Test that a Note object has the expected colour.
        note = Note.objects.get(id=1)
        colour = Colour.objects.get(id=1)
        self.assertEqual(note.colour, colour)


# Tests for Note views.
class NoteViewTest(TestCase):
    def setUp(self):
        # Create an Author object.
        author = Author.objects.create(name='Test Author')

        # Create a Colour object.
        colour = Colour.objects.create(colour_name='yellow')

        # Create a Note object for testing views.
        Note.objects.create(title='Test Note',
                            content='This is a test note.',
                            author=author, colour=colour)

    def test_note_list_view(self):
        # Test the "note list" view.
        response = self.client.get(reverse('note_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Note')

    def test_note_detail_view(self):
        # Test the "note detail" view.
        note = Note.objects.get(id=1)
        response = self.client.get(reverse('note_detail', args=[str(note.id)]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Note')
        self.assertContains(response, 'This is a test note.')

    def test_note_list_by_author_view(self):
        # Test the "note list by author" view.
        note = Note.objects.get(id=1)
        response = self.client.get(reverse('note_list_by_author',
                                           args=[note.author]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Note')
        self.assertContains(response, 'This is a test note.')

    def test_note_list_by_colour_view(self):
        # Test the "note list by colour" view.
        note = Note.objects.get(id=1)
        response = self.client.get(reverse('note_list_by_colour',
                                           args=[note.colour]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Note')
        self.assertContains(response, 'This is a test note.')
