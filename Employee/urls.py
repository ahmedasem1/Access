from django.urls import path

from . import views

urlpatterns = [
    path("singleemp/<int:group_id>/", views.SingleEmpView, name="employee"),
    path("jobs", views.Alljobsview, name="jobs"),
    path("signupemp", views.SignUpEmpView, name="signupemp"),
    path("profileemp/<int:pro_id>/", views.ProfileEmpView, name="profileemp"),
    path("registerexp/<int:pro_id>/", views.RegisterExpView, name="registerexp"),





]
