from django.test import SimpleTestCase
from django.urls import resolve, reverse
from Employee.views import *


class TestUrls(SimpleTestCase):
    def test_SignUpEmp_is_resolved(self):
        url = reverse("signupemp")
        self.assertEquals(resolve(url).func, SignUpEmpView)

    def test_SingleEmp_is_resolved(self):
        url = reverse("employee", args=["1"])
        self.assertEquals(resolve(url).func, SingleEmpView)

    def test_Joblist_is_resolved(self):
        url = reverse("jobs")
        self.assertEquals(resolve(url).func, Alljobsview)
