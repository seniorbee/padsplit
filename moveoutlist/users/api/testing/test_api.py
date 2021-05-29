from django.contrib.auth import get_user_model
from django.urls import NoReverseMatch
from rest_framework.reverse import reverse

from rest_framework.test import APITestCase, APIClient

USER_MODEL = get_user_model()


class TestUsersAPI(APITestCase):
    def setUp(self) -> None:
        self.user_data = {
            "email": "ali@admin.com",
            "password": "@lexand3R"
        }
        self.client = APIClient()

    def test_has_registration_url(self):
        try:
            reverse('users:register')
        except NoReverseMatch:
            self.fail('Add url for registration')

    def test_has_login_url(self):
        try:
            reverse('users:login')
        except NoReverseMatch:
            self.fail('Add url for login')

    def test_can_register(self):
        response = self.client.post(reverse('users:register'), data=self.user_data)
        self.assertContains(response, 'email', status_code=201)

    def test_can_login(self):
        self.client.post(reverse('users:register'), data=self.user_data)
        response = self.client.post(reverse('users:login'), data=self.user_data)
        self.assertContains(response, 'access', status_code=200)
