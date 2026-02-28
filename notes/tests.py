from django.test import TestCase
from django.urls import reverse
from .models import Note

class StickyNoteTests(TestCase):
    def setUp(self):
        # Create a sample note for Read/Delete tests
        self.note = Note.objects.create(title="Test Note", content="Testing logic")

    def test_note_creation(self):
        """Test if the model saves data correctly"""
        self.assertEqual(self.note.title, "Test Note")
        self.assertEqual(str(self.note), "Test Note")

    def test_list_view(self):
        """Test if the homepage loads and shows notes"""
        # Ensure 'note_list' matches the 'name' in your notes/urls.py
        response = self.client.get(reverse('note_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Note")

    def test_create_post(self):
        """Test creating a note via the form redirecting to list"""
        response = self.client.post(reverse('note_create'), {
            'title': 'New Note',
            'content': 'New Content'
        })
        self.assertRedirects(response, reverse('note_list'))
        self.assertEqual(Note.objects.count(), 2)

    def test_delete_post(self):
        """Test removing a note"""
        response = self.client.post(reverse('note_delete', args=[self.note.id]))
        self.assertRedirects(response, reverse('note_list'))
        self.assertEqual(Note.objects.count(), 0)
