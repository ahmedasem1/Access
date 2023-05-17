from django.test import SimpleTestCase
from django.urls import resolve, reverse
from Authentication.views import *


class TestUrls(SimpleTestCase):
    def test_list_is_resolved(self):
        url = reverse("login")
        self.assertEquals(resolve(url).func, LoginPage)

    def test_Signup_is_resolved(self):
        url = reverse("signup")
        self.assertEquals(resolve(url).func, SignupPage)
