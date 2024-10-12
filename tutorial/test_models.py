from django.db import IntegrityError
from django.contrib.auth.models import User
from django.test import TestCase
from .models import Tutorial, TutorialDate, Booking


class TestTutorialModel(TestCase):

    def setUp(self):
        """Set up data for TutorialDate model testing."""

        self.tutorial = Tutorial(
            title="Tutorial title",
            slug="tutorial-title",
            tutor_name="Tutor name",
            excerpt="Tutorial excerpt",
            description="Tutorial description",
            )
        self.tutorial.save()

    def test_tutorial_model_string(self):
        """Test tutorial model string."""

        self.assertEqual(str(self.tutorial), "Tutorial title")

    def test_tutorial_slug_is_unique(self):
        """Checks that tutorial slug is unique"""
        another_tutorial = Tutorial(
            title="Tutorial title2",
            slug="tutorial-title",
            tutor_name="Tutor name",
            excerpt="Tutorial excerpt",
            description="Tutorial description",
        )

        with self.assertRaises(IntegrityError):
            another_tutorial.save()

    def test_tutorial_title_is_unique(self):
        """Checks that tutorial slug is unique"""
        another_tutorial = Tutorial(
            title="Tutorial title",
            slug="tutorial-title2",
            tutor_name="Tutor name",
            excerpt="Tutorial excerpt",
            description="Tutorial description",
        )

        with self.assertRaises(IntegrityError):
            another_tutorial.save()


class TestTutorialDateModel(TestCase):
    def setUp(self):
        """Set up data for TutorialDate model testing."""

        self.tutorial = Tutorial.objects.create(title="Test tutorial title")
        self.tutorial_instance = TutorialDate.objects.create(
            tutorial_date="2024-10-31",
            start_time="09:00",
            end_time="11:00",
            tutorial=self.tutorial,
            )

    def test_tutorial_instance_is_created(self):
        """Test that Tutorial Date model instance is created."""

        self.assertEqual(
            self.tutorial_instance.tutorial_date,
            "2024-10-31"
        )
        self.assertEqual(
            self.tutorial_instance.start_time,
            "09:00"
        )
        self.assertEqual(
            self.tutorial_instance.end_time,
            "11:00"
        )
        self.assertEqual(
            str(self.tutorial_instance.tutorial),
            "Test tutorial title"
        )
        self.assertTrue(isinstance(self.tutorial_instance, TutorialDate))


class TestBookingModel(TestCase):
    def setUp(self):
        """Set up data for Booking model testing."""

        self.tutorial = Tutorial.objects.create(
            title="Tutorial title",
        )
        self.tutorial_instance = TutorialDate.objects.create(
            tutorial_date="2024-10-31",
            start_time="09:00",
            end_time="11:00",
            tutorial=self.tutorial,
            )
        self.user = User.objects.create_user(
            username='testuser',
            password='password'
        )
        self.booking = Booking.objects.create(
            tutorial_date=self.tutorial_instance,
            user=self.user
        )

    def test_booking_model_string(self):
        """testing booking model string"""
        self.assertEqual(
            str(self.booking),
            "2024-10-31 | 09:00 | Tutorial title | testuser"
        )

    def test_booking_instance_is_created(self):
        """Test if booking instance is created"""
        self.assertEqual(
            str(self.booking.tutorial_date),
            "2024-10-31 | 09:00 | Tutorial title"
            )
        self.assertEqual(self.booking.user, self.user)
        self.assertTrue(isinstance(self.booking, Booking))
 