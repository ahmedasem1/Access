from django.test import TestCase
from Employee.models import *


class TestModels(TestCase):
    def test_slug_emp(self):
        emp = Employee.objects.create(
            first_name="ahmed",
            last_name="asem",
            street="street",
            city="city",
            postal_code=0000,
            description="description",
            Dob="2023-05-10",
            contanct_number="01159885855",
            feild="feild",
            author="aasem8059@gmail.com",
        )
        emp.save()
        self.assertEquals(emp.slug, "ahmed-asem")
