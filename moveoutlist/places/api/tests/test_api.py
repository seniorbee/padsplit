from django.contrib.auth import get_user_model

from rest_framework.test import APITestCase, APIClient

USER_MODEL = get_user_model()


# Create your testing here.
# class TestMoveOuts(APITestCase):
#     def setUp(self) -> None:
#
#     def test_can_create_move_out