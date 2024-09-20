from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .forms import TutorialForm, TutorialDateForm

# Create your tests here.


class TestTutorialForm(TestCase):

    def test_form_is_valid(self):
        """
        method that tests TutorialForm.
        """
        tutorial_form = TutorialForm({
            'title': 'title name',
            'slug': 'title-name',
            'description': 'description',
            'tutor_name': 'tutor name',
            'excerpt':'excerpt',},
            {'image':
             SimpleUploadedFile(
                 name='test_image.jpg',
                 content=b'd',
                 content_type='image/jpeg'
                 )
            })
        
        self.assertTrue(tutorial_form.is_valid())

