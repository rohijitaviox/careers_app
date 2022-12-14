from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.test import APITestCase


class TestUserViews(APITestCase):
    """Tests creating user,login,logout, updating user,partial updating user,\
        retrieving user and deleting user"""

    def setUp(self) -> None:
        self.create_user_data = {
            'first_name': 'TestFirstName',
            "last_name": 'TestLastName',
            'email': 'test@test.com',
            'username': 'test@test.com',
            'password': 'SomeLongPassword@12345'
        }
        self.user_url = reverse("accounts:user")
        self.login_url = reverse("accounts:login")

    def test_user_creation(self):
        res = self.client.post(
            self.user_url, self.create_user_data, format='json')
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = User.objects.filter(username=self.create_user_data['username'])
        self.assertEqual(user.count(), 1)
        # FOr failed request in case of signing up again
        res_failed = self.client.post(
            self.user_url, self.create_user_data, format='json')
        self.assertEqual(res_failed.status_code, status.HTTP_400_BAD_REQUEST)

    def get_user_token(self):
        user = User.objects.create_user(**self.create_user_data)
        token = Token.objects.create(user=user)
        return token.key

    def test_user_login(self):
        User.objects.create_user(**self.create_user_data)
        login_data = {
            'email': self.create_user_data['email'],
            'password': self.create_user_data['password']
        }
        res = self.client.post(self.login_url, login_data, format='json')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIn("token", res.json())
        # For incorrect email
        login_data_email = login_data
        login_data_email['email'] = login_data['email']+"com"
        res_incorrect_email = self.client.post(
            self.login_url, login_data_email, format='json')
        self.assertEqual(res_incorrect_email.status_code,
                         status.HTTP_401_UNAUTHORIZED)
        # for incorrect password
        login_data_pw = login_data
        login_data_pw['password'] = login_data['password']+"jjjj"
        res_incorrect_pw = self.client.post(
            self.login_url, login_data_pw, format='json')
        self.assertEqual(res_incorrect_pw.status_code,
                         status.HTTP_401_UNAUTHORIZED)

    def test_user_update(self):
        token = self.get_user_token()
        update_data = self.create_user_data
        update_data['first_name'] = "UpdatedTestFirstName"
        update_data.pop('password', None)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
        res = self.client.put(self.user_url, update_data, format="json")
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        user = User.objects.get(username=update_data['username'])
        self.assertEqual(user.first_name, update_data['first_name'])

    def test_user_retrieve(self):
        token = self.get_user_token()
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
        res = self.client.get(self.user_url)
        data = {
            "first_name": "TestFirstName",
            "last_name": "TestLastName",
            "username": "test@test.com",
            "email": "test@test.com"
        }
        self.assertDictEqual(res.json(), data)

    def test_logout(self):
        token = self.get_user_token()
        logout_url = reverse("accounts:logout")
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
        res = self.client.get(logout_url)
        user = User.objects.get(username=self.create_user_data['username'])
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        token = Token.objects.filter(user=user)
        self.assertEqual(token.count(), 0, msg="Token was not deleted")

    def test_delete(self):
        data = {
            'email': self.create_user_data['email'],
            'password': self.create_user_data['password']
        }
        token = self.get_user_token()
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
        res = self.client.delete(self.user_url, data=data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
