from django.shortcuts import get_object_or_404, render
from .models import Company,Job
from Employee.models import Employee
from django.shortcuts import render,HttpResponse,redirect





def SignUpComView(request):
    if request.method == "POST":
        name = request.POST.get("name")

        street = request.POST.get("street")
        postal_code = request.POST.get("postal_code")
        city = request.POST.get("city")

        image = request.FILES.get("image")

        description = request.POST.get("description")
        Dob = request.POST.get("Dob")
        contanct_number = request.POST.get("contanct_number")

        feild = request.POST.get("feild")
        rating = request.POST.get("rating")
        date = request.POST.get("date")

        my_com = Company.objects.create(
            name=name,
            image=image,
            street=street,
            city=city,
            postal_code=postal_code,
            description=description,
            Dob=Dob,
            contanct_number=contanct_number,
            feild=feild,
            rating=rating,
            date=date,
            author=request.user.username,
        )
        my_com.save()

    return render(request, "Company/SignUpCom.html")

def SingleComView(request, group_id):
    context = Company.objects.filter(author=request.user.username).first()
    if context is None:
        context = Employee.objects.filter(author=request.user.username).first()
        
    company = Company.objects.filter(id=group_id).first()
    jobs=Job.objects.filter(company=company)
    fill_relations = {"company": company, "context": context,"jobs":jobs}
    return render(request, "Company/SingleCom.html", fill_relations)

def AllComView(request):
    context = Company.objects.filter(author=request.user.username).first()
    if context is None:
        context = Employee.objects.filter(author=request.user.username).first()
        
    company = Company.objects.all()
    fill_relations = {"companys": company, "context": context}
    return render(request, "Company/AllCom.html", fill_relations)

def SingleJobView(request, job_id):
    if request.method == "POST":
        print("88888888888888888")
        context = Employee.objects.get(author=request.user.username)
        jobs=Job.objects.get(id=job_id)
        jobs.Employees.add(context)
        print(context)
        print(jobs)
        # jobs.save()
        print("88888888888888888")
        x=jobs.Employees
        print(x)

        return redirect('jobs')
    if request.method == "GET":

        context = Company.objects.filter(author=request.user.username).first()
        if context is None:
            context = Employee.objects.filter(author=request.user.username).first()
        jobs=Job.objects.filter(id=job_id).first()
            
        company = jobs.company
        
        
    
        fill_relations = {"company":company,"context": context,"job":jobs}
        return render(request, "Company/SingleJob.html", fill_relations)   

    
