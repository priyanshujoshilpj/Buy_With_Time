from .models import UserModel
from django.http import response
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate




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

class SignUpPageTests(TestCase):
    def setUp(self) -> None:
        self.username = 'testuser'
        self.fname = 'yashas'
        self.lname = 'grover'
        self.email = 'testuser@email.com'
        self.pass1 = 'password'
        self.pass2 = 'password'

    def test_signup_page_view_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='users/signup.html')

    
    def test_signup_form(self):
        response = self.client.post(reverse('signup'), data={
            'username': self.username,
            'fname' : self.fname,
            'lname' : self.lname,
            'email': self.email,
            'pass1': self.pass1,
            'pass2': self.pass2,
        })
        self.assertEqual(response.status_code, 302)

        users = UserModel.objects.all()
        self.assertEqual(users.count(), 1)


