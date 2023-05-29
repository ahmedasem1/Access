from django.test import TestCase, Client
from django.urls import reverse


class test_views_access(TestCase):

    def test_SignUpComView_GET(self):
        client = Client()
        response = client.get(reverse("signupcomp"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "Company/SignUpCom.html")
