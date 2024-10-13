from django.test import TestCase
from tutorial.models import Tutorial, TutorialDate
from .forms import BookingForm


class TestBookingForm(TestCase):
    def setUp(self):
        """Set up for form testing"""
        self.tutorial = Tutorial.objects.create(title="tutorial title")
        self.tutorial_date = TutorialDate.objects.create(
            tutorial=self.tutorial,
            tutorial_date="2024-10-31",
            start_time="09:00",
            end_time="11:00",
        )

    def test_form_is_valid(self):
        """Testing form with available tutorial option"""

        booking_form = BookingForm({'tutorial_date': self.tutorial_date.id})
        self.assertTrue(booking_form.is_valid(), msg="Form is not valid")

    def test_form_no_option(self):
        """Testing form with no tutorial option"""

        booking_form = BookingForm({'tutorial_date': ''})
        self.assertFalse(booking_form.is_valid(), msg="Form is valid")
