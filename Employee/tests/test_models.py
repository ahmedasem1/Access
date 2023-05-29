from django.test import TestCase
from Employee.models import *


class TestModels(TestCase):
    def setUp(self):
        Employee.objects.create(
                    first_name="ahmed",
                    last_name="asem",
                    street="street",
                    city="city",
                    postal_code=0000,
                    description="description",
                    Dob="2023-05-10",
                    contanct_number="01159885855",
                    feild="feild",
                    author="aasem8059@gmail.com",)     
    def test_slug_emp(self):
        emp = Employee.objects.get(author="aasem8059@gmail.com")
        self.assertEquals(emp.first_name, "ahmed")
