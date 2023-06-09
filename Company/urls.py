from django.urls import path

from . import views

urlpatterns = [
    path("company/<int:group_id>/", views.SingleComView, name="company"),
    path("companys", views.AllComView, name="companys"),
    path("signupcomp", views.SignUpComView, name="signupcomp"),
    path("job/<int:job_id>/", views.SingleJobView, name="SingleJob"),
    path("home",  views.HomeComView, name="home_com"),
    path("appliedemp/<int:job_id>/",  views.AppEmpView, name="appliedemp"),
    path("registerjob", views.RegisterJobView, name="registerjob"),
]
