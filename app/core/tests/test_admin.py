from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from rest_framework import status


class AdminSiteTests(TestCase):

    def setUp(self):
        # Create a superuser and log him in
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='pako@test.com',
            password='maskoanmsi'
        )
        self.client.force_login(self.admin_user)

        self.user = get_user_model().objects.create_user(
            email='koko@loko.com',
            password='as54affcv',
            # name='koko loko'
        )

    def test_users_listed(self):
        """Tests that users are listed in user page."""
        url = reverse('admin:core_user_changelist')
        # reverse(admin:<app>_<model>_changelist
        # https://docs.djangoproject.com/en/3.0/ref/contrib/admin/#reversing-admin-urls
        response = self.client.get(url)

        self.assertContains(response, self.user.name)
        self.assertContains(response, self.user.email)

    def test_user_change_page(self):
        """Test that the user edit page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_add_page(self):
        """Test that the user add page is displayed"""
        url = reverse('admin:core_user_add')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
