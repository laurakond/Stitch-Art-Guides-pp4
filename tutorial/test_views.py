from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .models import Tutorial

# This test was appropriated from Code Institute's I think I blog walkthrough
# noted in the README.md


class TestTutorialViews(TestCase):

    def setUp(self):
        """Set up for testing Tutorial views."""
        self.user = User.objects.create_superuser(
            username="username",
            password="password",
            email="email@email.com"
        )
        self.tutorial = Tutorial(
            title="Tutorial title",
            slug="tutorial-title",
            tutor_name="Tutor name",
            excerpt="Tutorial excerpt",
            description="Tutorial description",
            )
        self.tutorial.save()

    def test_render_tutorial_detail_page(self):
        response = self.client.get(reverse(
            'tutorial_detail', args=['tutorial-title']))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Tutorial title", response.content)
        self.assertIn(b"Tutorial description", response.content)
