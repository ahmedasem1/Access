from django.test import TestCase
from Company.models import *


class TestModels(TestCase):
    def test_slug_com(self):
        com = Company.objects.create(
            name="microsoft teams",
            street="street",
            city="city",
            postal_code=0000,
            description="description",
            date="2023-05-10",
            contanct_number="01159885855",
            feild="feild",
            author="aasem8059@gmail.com",
        )
        com.save()
        self.assertEquals(com.name, "microsoft teams")
