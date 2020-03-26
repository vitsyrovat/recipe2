from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

# from rest_framework import status


class ModelTests(TestCase):

    def test_user_with_email_created(self):
        """Test that a user with an email is created"""
        email = 'pako@email.cz'
        password = 'jksj12af22'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test that new user email is normalized"""
        email = 'test@LONDON.COM'
        user = get_user_model().objects.create_user(
            email, 'asd321asd'
        )

        self.assertEqual(email.lower(), user.email)

    def test_new_user_no_email(self):
        """Test creating user with no email raises error"""
        email = None
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email, 'asdjhfksjdh'
            )

    def test_new_user_valid_email(self):
        """Test creating new user with an invalid email raises error"""

        email1 = 'oijo@'
        email2 = 'koko@loko'
        email3 = '--'

        with self.assertRaises(ValidationError):
            get_user_model().objects.create_user(email1, 'ksdfjklsldk')
        with self.assertRaises(ValidationError):
            get_user_model().objects.create_user(email2, 'lsdkjfou5i')
        with self.assertRaises(ValidationError):
            get_user_model().objects.create_user(email3, 'laksflks11d')
