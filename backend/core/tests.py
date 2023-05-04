from .models import Contact
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework import status

class ContactTestCase(APITestCase):
    """
    Test suite for Contact
    """
    def setUp(self) -> None:
        self.client = APIClient()
        self.data = {
            "name": "Samarendra Behera",
            "message": "This is a test message",
            "email": "samarendra@example.com"
        }
        self.url = '/contact/'
    def test_create_contact(self):
        '''
        test ContactViewSet create method
        '''
        data = self.data
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Contact.objects.count(), 1)
        self.assertEqual(Contact.objects.get().title, "Samarendra Behera")
    def test_create_contact_without_name(self):
        '''
        test ContactViewSet create method when name is not in data
        '''
        data = self.data
        data.pop('name')
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    def test_create_contact_when_name_equals_blank(self):
        '''
        test ContactViewSet create method when name is not in data
        '''
        data = self.data
        data['name'] = ""
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    def test_create_contact_without_message(self):
        '''
        test ContactViewSet create method when name is not in data
        '''
        data = self.data
        data.pop('message')
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    def test_create_contact_without_email(self):
        '''
        test ContactViewSet create method when name is not in data
        '''
        data = self.data
        data.pop('email')
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    def test_create_contact_when_email_equals_blank(self):
        '''
        test ContactViewSet create method when name is not in data
        '''
        data = self.data
        data['email'] = ''
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    def test_create_contact_when_email_equals_non_email(self):
        '''
        test ContactViewSet create method when name is not in data
        '''
        data = self.data
        data['email'] = 'test'
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)