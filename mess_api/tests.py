from django.test import TestCase
from rest_framework.test import APIRequestFactory, APIClient
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from . import views

# Create your tests here.
class AccessIsCorrect(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_unauthorized_user_cant_access(self):
        response = self.client.post('/createuser/', {"username":"teskt", "password":"pass"})
        self.assertEqual(response.status_code, 201)
        self.client.force_authenticate(get_user_model().objects.get(id=response.data['id']))
        response = self.client.post('/createconversation/', {"conversation_name": "testingconv"})
        response = self.client.get('/conversations/' + str(response.data['id']))
        self.assertEqual(response.status_code, 403)

    def test_authorized_user_can_access(self):
        response = self.client.post('/createuser/', {"username":"teskt", "password":"pass"})
        self.assertEqual(response.status_code, 201)
        user_id = response.data['id']
        test_user = get_user_model().objects.get(id=user_id)
        self.client.force_authenticate(test_user)
        response = self.client.post('/createconversation/', {"conversation_name": "testingconv", "user_set": ["http://localhost:8000/users/" + str(user_id) + "/"]})
        response = self.client.get('/conversations/' + str(response.data['id']))
        self.assertEqual(response.status_code, 200)

        