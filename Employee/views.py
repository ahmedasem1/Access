from django.contrib.messages import constants as messages
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Employee, Main_skill, Pluses
from Company.models import Job


# filling the employee data


def SignUpEmpView(request):
    main = Main_skill.objects.all()
    plus = Pluses.objects.all()

    fill_relations = {"main": main, "plus": plus}

    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")

        street = request.POST.get("street")
        postal_code = request.POST.get("postal_code")
        city = request.POST.get("city")

        image = request.POST.get("image")

        description = request.POST.get("description")
        Dob = request.POST.get("Dob")
        contanct_number = request.POST.get("contanct_number")

        feild = request.POST.get("feild")

        skills = request.POST.get("skills")
        pluse = request.POST.get("pluse")

        my_emp = Employee.objects.create(
            first_name=first_name,
            last_name=last_name,
            image=image,
            street=street,
            city=city,
            postal_code=postal_code,
            description=description,
            Dob=Dob,
            contanct_number=contanct_number,
            feild=feild,
            author=request.user.username,
        )
        my_emp.Main_skills.set(skills)
        my_emp.Pluses.set(pluse)

        my_emp.save()

    return render(request, "Employee/SignUpEmp.html", fill_relations)


# display each employee profile


class SingleEmpView(DetailView):
    template_name = "Employee/SingleEmp.html"
    model = Employee


# displaying all jobs related to each employee


class JobsListView(ListView):
    template_name = "Employee/Jobs.html"
    model = Job
    context_object_name = "jobs"

    def get_context_data(self, *args, **kwargs):
        # Call the base implementation first to get a context
        context = super(JobsListView, self).get_context_data(**kwargs)
        context = Employee.objects.filter(author=self.request.user.username).first()
        context = {"context": context}
        print(context)
        return context
