from django.contrib import admin
from Employee.models import Main_skill, Pluses, Employee
from .models import Exp



admin.site.register(Main_skill)
admin.site.register(Pluses)
admin.site.register(Employee)
admin.site.register(Exp)

