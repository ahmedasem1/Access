from django.shortcuts import get_object_or_404, render
from .models import Company,Job
from Employee.models import Employee





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
    print(jobs)
    fill_relations = {"company": company, "context": context,"jobs":jobs}
    return render(request, "Company/SingleCom.html", fill_relations)