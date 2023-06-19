from django.urls import path

from . import views

urlpatterns = [
    path("singleemp/<int:group_id>/", views.SingleEmpView, name="employee"),
    path("jobs", views.Alljobsview, name="jobs"),
    path("signupemp", views.SignUpEmpView, name="signupemp"),


]
