from django.test import TestCase
from notes.models import Note

class TestNoteModel(TestCase):

    def setUp(self):
        self.data1 = Note.objects.create(title='django')

    def test_note_model_entry(self):
        """
        Test Category model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Note))
        self.assertEqual(str(data), 'django')
