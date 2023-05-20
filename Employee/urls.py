
from django.urls import path

from . import views

urlpatterns = [
    path("employee/<int:pk>/", views.SingleEmpView.as_view(), name="employee"),
    path("jobs", views.Alljobsview, name="jobs"),
    path("signupemp", views.SignUpEmpView, name="signupemp"),
]
