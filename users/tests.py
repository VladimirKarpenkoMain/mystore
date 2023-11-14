from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from users.models import User


class UserRegistrationViewTestCase(TestCase):

    def setUp(self) -> None:
        self.path = reverse('users:registration')

    def test_user_registration_get(self):
        response = self.client.get(self.path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'users/register.html')

    def test_user_registration_post_success(self):
        data = {
            'first_name': 'Oleg', 'last_name': "Petrov",
            'username': 'safgka', 'email': 'afo2msa@mail.ru',
            'password1': 'agdjasdfk2134r8', 'password2': 'agdjasdfk2134r8'
        }
        username = data['username']
        self.assertFalse(User.objects.filter(username=username).exists())
        response = self.client.post(self.path, data)

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse('users:login'))
        self.assertTrue(User.objects.filter(username=username).exists())
