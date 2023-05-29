from django.test import TestCase, Client
from django.urls import reverse


class test_views_access(TestCase):

    def test_JobsView_GET(self):
        client = Client()
        response = client.get(reverse("jobs"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "Jobs.html")

    def test_SignUpEmpView_GET(self):
        client = Client()
        response = client.get(reverse("signupemp"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "SignUpEmp.html")    

