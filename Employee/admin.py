from django.contrib import admin
from Employee.models import Main_skill,  Employee
from .models import Exp



admin.site.register(Main_skill)
admin.site.register(Employee)
admin.site.register(Exp)

