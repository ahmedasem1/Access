from django.contrib.messages import constants as messages
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Employee, Main_skill, Pluses,Exp
from Company.models import Job,Company
from django.shortcuts import render, redirect


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

        image = request.FILES.get("image")

        description = request.POST.get("description")
        Dob = request.POST.get("Dob")
        contanct_number = request.POST.get("contanct_number")

        feild = request.POST.get("feild")

        skills = request.POST.getlist("skills")
        pluse = request.POST.getlist("pluse")

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
        return redirect("jobs")


    return render(request, "Employee/SignUpEmp.html", fill_relations)

# displaying all jobs related to each employee


def Alljobsview(request):
    employee = Employee.objects.filter(author=request.user.username).first()
    if request.method == "POST":
        jobs = Job.objects.filter(title__contains=request.POST.get("form-control me-2"))
    if request.method == "GET":
        jobs = Job.objects.all()

        x=0
        for job in jobs:
            for skill in job.Main_skill.all():
                if skill in employee.Main_skills.all():
                    x=x+1
            job.order=x
            job.save()

            
                    
        jobs = Job.objects.order_by('order')


    fill_relations = {"employee": employee, "jobs": jobs}
    return render(request, "Employee/Jobs.html", fill_relations)

# displaying single employee profile

def SingleEmpView(request, group_id):
    context = Company.objects.filter(author=request.user.username).first()
    employee = Employee.objects.filter(id=group_id).first()
    experience= Exp.objects.filter(emp=employee).all()

    if context is None:
        context = Employee.objects.filter(author=request.user.username).first()
        if context.id==employee.id:
            return redirect('profileemp',pro_id=group_id)

    
    

    fill_relations = {"employee": employee, "context": context,"experience":experience}
    return render(request, "Employee/SingleEmp.html", fill_relations)

def ProfileEmpView(request, pro_id):
    context = Employee.objects.filter(author=request.user.username).first()
    employee = Employee.objects.filter(id=pro_id).first()
    experience= Exp.objects.filter(emp=employee).all()

    fill_relations = {"employee": employee, "context": context,"experience":experience}
    return render(request, "Employee/profileemp.html", fill_relations)

def RegisterExpView(request,pro_id):
    context = Employee.objects.filter(author=request.user.username).first()   
    if request.method == "POST":
        title = request.POST.get("title")
        # context = Company.objects.filter(author=request.user.username).first()   
        description = request.POST.get("description")
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")


        feild = request.POST.get("feild")
        type = request.POST.get("type")
        company = request.POST.get("company")


        my_Exp= Exp.objects.create(
            title=title,
            company=company,
            description=description,
            feild=feild,
            type=type,
            Employee=context,
            start_date=start_date,
            end_date=end_date,
        )

        my_Exp.save()
        return redirect('profileemp',pro_id=pro_id)
    company = Company.objects.all()

    fill_relations = {"companys": company, "context": context}
    return render(request, "Employee/RegisterExp.html", fill_relations)
