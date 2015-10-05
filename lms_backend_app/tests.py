from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status

# Create your tests here.
factory = APIRequestFactory()

request = factory.post(
    '/users/',
    {'inmate_id', '112039'},
    format='json'
    );
