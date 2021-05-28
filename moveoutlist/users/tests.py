from django.contrib.auth import login
from django.contrib.auth.hashers import check_password
from django.db import IntegrityError
from django.test import TestCase

from users.models import User


# Create your tests here.
class UserTestCase(TestCase):
    def setUp(self):
        self.user_data = {'email': 'gubatovalihaydar@gmail.com', 'password': 'AnewPas923'}
        self.user = User.objects.create_user(**self.user_data)

    def test_user_count(self):
        self.assertEqual(User.objects.count(), 1)

    def test_user_password_not_plain(self):
        self.assertNotEqual(self.user.password, self.user_data['password'])

    def test_user_unique(self):
        with self.assertRaises(IntegrityError):
            User.objects.create_user(**self.user_data)

    def test_user_can_login(self):
        self.assertEqual(self.user.check_password(self.user_data['password']), True)
