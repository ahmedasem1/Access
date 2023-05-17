from django.test import TestCase, Client
from django.urls import reverse
from Company.models import Company


class test_views_access(TestCase):
    def test_SingleComView_GET(self):
        client = Client()
        response = client.get(reverse("company", args=["1"]))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "Company/SingleCom.html")

    def test_SignUpComView_GET(self):
        client = Client()
        response = client.get(reverse("signupcomp"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "Company/SignUpCom.html")
