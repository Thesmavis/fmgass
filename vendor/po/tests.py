from django.test import TestCase
from rest_framework.test import APIRequestFactory,APITestCase,URLPatternsTestCase
from django.urls import path,include
from rest_framework import status

# Create your tests here.
factory= APIRequestFactory()
# request = factory.post('/POST/api/vendors/',{},format='json')

class vendortests(APITestCase,URLPatternsTestCase):
    urlpatterns = [
 
    path('',include('po.urls')),
]
    def test_create(self):

        response=self.client.get('GET/api/vendors/',format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(len(response.data),1)

