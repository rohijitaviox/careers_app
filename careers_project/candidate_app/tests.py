from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from models_app.models.candidateModel import Candidate


class CandidateApiTestCase(APITestCase):
    """Tests creating user,login,logout, updating user,partial updating user,\
        retrieving user and deleting user"""
    def setUp(self) -> None:
        self.create_user_data = {
            'first_name': 'TestFirstName',
            "last_name": 'TestLastName',
            'email': 'test@test.com',
            'address': 'test@test.com',
            'position': 'developer',
            'profile_pic':'/media/new/image.png',
            'higher_education':'graduation',
            'contact_no':12342546676,
            'experience':'2',
            'black_list':False
        }
        self.candidate_url = reverse("candidate:api")
    
    def test_candidate_creation(self):
        res = self.client.post(
            self.candidate_url, self.create_user_data, format='json')
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = Candidate.objects.filter(username=self.create_user_data['username'])
        self.assertEqual(user.count(), 1)
        # For failed request in case of signing up again
        res_failed = self.client.post(
            self.user_url, self.create_user_data, format='json')
        self.assertEqual(res_failed.status_code, status.HTTP_400_BAD_REQUEST)
