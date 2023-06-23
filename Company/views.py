from django.shortcuts import get_object_or_404, render
from .models import Company,Job
from Employee.models import Employee,Main_skill,Pluses
from django.shortcuts import render,HttpResponse,redirect





def SignUpComView(request):
    if request.method == "POST":
        name = request.POST.get("name")

        street = request.POST.get("street")
        postal_code = request.POST.get("postal_code")
        city = request.POST.get("city")

        image = request.FILES.get("image")

        description = request.POST.get("description")
        contanct_number = request.POST.get("contanct_number")

        feild = request.POST.get("feild")
        Dob = request.POST.get("Dob")

        my_com = Company.objects.create(
            name=name,
            image=image,
            street=street,
            city=city,
            postal_code=postal_code,
            description=description,
            contanct_number=contanct_number,
            feild=feild,
            date=Dob,
            author=request.user.username,
        )
        my_com.save()

    return render(request, "Company/SignUpCom.html")

# every single company page

def SingleComView(request, group_id):
    context = Company.objects.filter(author=request.user.username).first()
    if context is None:
        context = Employee.objects.filter(author=request.user.username).first()
        
    company = Company.objects.filter(id=group_id).first()
    jobs=Job.objects.filter(company=company)
    fill_relations = {"company": company, "context": context,"jobs":jobs}
    return render(request, "Company/SingleCom.html", fill_relations)

# page contains all companies

def AllComView(request):
    context = Company.objects.filter(author=request.user.username).first()
    if context is None:
        context = Employee.objects.filter(author=request.user.username).first()
        
    company = Company.objects.all()
    fill_relations = {"companys": company, "context": context}
    return render(request, "Company/AllCom.html", fill_relations)

# every single job page and employee can apply

def SingleJobView(request, job_id):
    if request.method == "POST":
        context = Employee.objects.get(author=request.user.username)
        jobs=Job.objects.get(id=job_id)
        jobs.Employees.add(context)
        return redirect('jobs')
    if request.method == "GET":

        context = Company.objects.filter(author=request.user.username).first()
        if context is None:
            context = Employee.objects.filter(author=request.user.username).first()
        jobs=Job.objects.filter(id=job_id).first()
            
        company = jobs.company
        
        
    
        fill_relations = {"company":company,"context": context,"job":jobs}
        return render(request, "Company/SingleJob.html", fill_relations)   

# regester a new job
    
def RegisterJobView(request):
    context = Company.objects.filter(author=request.user.username).first()   
    main = Main_skill.objects.all()
    if request.method == "POST":
        title = request.POST.get("title")
        skills = request.POST.getlist("skills")
        context = Company.objects.filter(author=request.user.username).first()   
        description = request.POST.get("description")

        feild = request.POST.get("feild")
        type = request.POST.get("type")

        my_job= Job.objects.create(
            title=title,
            company=context,
            description=description,
            feild=feild,
            type=type,
        )
        my_job.Main_skill.set(skills)

        my_job.save()
        return redirect("home_com")

    company = Company.objects.all()

    fill_relations = {"companys": company, "context": context,"main":main}
    return render(request, "Company/RegisterJob.html", fill_relations)

# displaying all jobs related to each employee


def HomeComView(request):
    company = Company.objects.filter(author=request.user.username).first()
    if request.method == "POST":
        jobs = Job.objects.filter(title__contains=request.POST.get("form-control me-2"))
    if request.method == "GET":
        jobs = Job.objects.filter(company=company)


    fill_relations = {"company": company, "jobs": jobs}
    return render(request, "Company/home_com.html", fill_relations)

def AppEmpView(request, job_id):
    company = Company.objects.filter(author=request.user.username).first()
    jobs = Job.objects.filter(id=job_id).first()

    if request.method == "POST":
        emp=jobs.Employees.all()
        x=request.POST.get("form-control me-2")
        first=x.split(" ")[0]
        last=x.split(" ")[1]
        employees = emp.filter(first_name__contains=first , last_name__contains=last)
    if request.method == "GET":
        jobs = Job.objects.filter(id=job_id).first()
        employees=jobs.Employees.all()
        x=0
        for employee in employees:
            for skill in employee.Main_skills.all():
                if skill in jobs.Main_skill.all():
                    x=x+1
                if skill not in employee.Main_skills.all():
                    x=x-1    
            employee.order=x
            employee.save()
        employee = Employee.objects.order_by('-order')

    fill_relations = {"company": company, "jobs": jobs,"employees":employees}
    return render(request, "Company/apply_jobs.html", fill_relations)