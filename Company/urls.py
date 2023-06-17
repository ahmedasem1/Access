from django.urls import path

from . import views

urlpatterns = [
    path("company/<int:group_id>/", views.SingleComView, name="company"),
    path("signupcomp", views.SignUpComView, name="signupcomp"),
    # path("registerjob", views.RegisterJobView, name="registerjob"),
]
