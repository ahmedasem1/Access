from django.db import models
from django.urls import reverse
import datetime
# from Company.models import Company


from django.utils.text import slugify


# Create your models here.
class Main_skill(models.Model):
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=500, null=True)

    def __str__(self):
        return f"{self.name}"


class Pluses(models.Model):
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=500, null=True)

    def __str__(self):
        return f"{self.name}"


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    image = models.ImageField(upload_to="images/", null=True)

    street = models.CharField(max_length=80, null=True)
    postal_code = models.CharField(max_length=5, null=True)
    city = models.CharField(max_length=50, null=True)

    description = models.TextField(max_length=2000)
    Dob = models.DateField(auto_now=False, auto_now_add=False)
    contanct_number = models.CharField(max_length=100)
    feild = models.CharField(max_length=200, null=True)
    author = models.EmailField(max_length=100, null=False)

    slug = models.SlugField(default="", blank=True, null=False, db_index=True)
    order=models.IntegerField(null=True)

    # relations
    Main_skills = models.ManyToManyField(Main_skill)
    Pluses = models.ManyToManyField(Pluses)

    def get_absolute_url(self):
        return reverse("employee", args=[self.id])

    def __str__(self):
        return f"{self.first_name} ({self.last_name})"



class Exp(models.Model):
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=500, null=True)
    start_date = models.DateField(
        auto_now=False, auto_now_add=False, null=True, blank=True
    )
    end_date = models.DateField(
        auto_now=False, auto_now_add=False, default=datetime.date.today()
    )
    company = models.CharField(max_length=500)

    # relations
    
    Employee = models.ForeignKey(Employee ,on_delete=models.CASCADE, default="5")

    def __str__(self):
        return f"{self.title}"