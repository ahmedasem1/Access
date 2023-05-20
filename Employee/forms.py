from django import forms

from .models import Employee


class SignUpEmpForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
        exclude = ["author"]