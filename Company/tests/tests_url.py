from django.test import SimpleTestCase
from django.urls import resolve, reverse
from Company.views import *


class TestUrls(SimpleTestCase):
    def test_SingleCom_is_resolved(self):
        url = reverse("company", args=["5"])
        self.assertEquals(resolve(url).func.view_class, SingleComView)

    def test_SignUpCom_is_resolved(self):
        url = reverse("signupcomp")
        self.assertEquals(resolve(url).func, SignUpComView)
