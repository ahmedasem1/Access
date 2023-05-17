from django.urls import path

from . import views

urlpatterns = [
    path("company/<int:pk>/", views.SingleComView.as_view(), name="company"),
    path("signupcomp", views.SignUpComView, name="signupcomp"),
    # path("registerjob", views.RegisterJobView, name="registerjob"),
]
