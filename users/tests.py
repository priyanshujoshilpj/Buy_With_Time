from django.http import response
from django.test import TestCase

# Create your tests here.

class URLTests(TestCase):
    def test_testhomepage(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
    
    def test_testsignup(self):
        response = self.client.get('/signup')
        self.assertEqual(response.status_code, 200)
    
    def test_testsignin(self):
        response = self.client.get('/signin')
        self.assertEqual(response.status_code, 200)

    
    def test_testaboutus(self):
        response = self.client.get('/aboutus')
        self.assertEqual(response.status_code, 200)

    def test_testcontactus(self):
        response = self.client.get('/contactus')
        self.assertEqual(response.status_code, 200)

    def test_testsignout(self):
        response = self.client.get('/signout')
        self.assertEqual(response.status_code, 302)
