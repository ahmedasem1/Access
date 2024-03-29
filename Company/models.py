from django.db import models
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
from django.apps import apps
import datetime

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=100)

    image = models.ImageField(upload_to="images/", null=True)
    

    street = models.CharField(max_length=80, null=True)
    postal_code = models.CharField(max_length=5, null=True)
    city = models.CharField(max_length=50, null=True)

    description = models.TextField(max_length=2000)



    contanct_number = models.CharField(max_length=100)
    feild = models.CharField(max_length=200, null=True)
    date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    author = models.EmailField(max_length=100, null=False)

    slug = models.SlugField(default="", blank=True, null=False, db_index=True)

    # relations
    def get_absolute_url(self):
        return reverse("company", args=[self.id])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Company, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.contanct_number})"


class Job(models.Model):
    title = models.CharField(max_length=100)

    description = models.TextField(max_length=2000)
    type = models.CharField(max_length=500, null=True)
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)
    feild = models.CharField(max_length=200, null=True)
    order= models.IntegerField(null=True)
    # relations
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    Main_skill = models.ManyToManyField("Employee.Main_skill")
    Employees = models.ManyToManyField("Employee.Employee", blank=True)

    def get_absolute_url(self):
        return reverse("SingleJob", args=[self.id])

    def __str__(self):
        return f"{self.title} ({self.company.name})"
    
