from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils.timezone import now

User = get_user_model()


class UserModelTests(TestCase):

    def test_create_user(self):
        """Test creating a regular user with a phone number."""
        mobile_number = "09123456789"
        password = "testpassword"
        user = User.objects.create(mobile_number=mobile_number, username=mobile_number)
        user.set_password(password)
        user.save()

        self.assertEqual(user.mobile_number, mobile_number)
        self.assertTrue(user.check_password(password))
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        """Test creating a superuser with a phone number."""
        mobile_number = "09123456789"
        password = "testpassword"
        user = User.objects.create_superuser(mobile_number=mobile_number, username=mobile_number, password=password)

        self.assertEqual(user.mobile_number, mobile_number)
        self.assertTrue(user.check_password(password))
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

    def test_username_defaults_to_mobile_number(self):
        """Test that the username defaults to the phone number."""
        mobile_number = "09123456789"
        user = User.objects.create_user(mobile_number=mobile_number, username=mobile_number, password="testpassword")

        self.assertEqual(user.username, mobile_number)

    def test_last_login_updates(self):
        """Test that the last_login field is updated on login."""
        mobile_number = "09123456789"
        password = "testpassword"
        user = User.objects.create_user(mobile_number=mobile_number, username=mobile_number, password=password)

        self.assertIsNone(user.last_login)

        # Simulate a login
        user.last_login = now()
        user.save()

        self.assertIsNotNone(user.last_login)
