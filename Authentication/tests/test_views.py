from django.test import TestCase, Client
from django.urls import reverse


class test_views_access(TestCase):
    def test_SignupPage_GET(self):
        client = Client()
        response = client.get(reverse("signup"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "authentication/signup.html")

    def test_LoginPage_GET(self):
        client = Client()
        response = client.get(reverse("login"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "authentication/login.html")
