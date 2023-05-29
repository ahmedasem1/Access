from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView
from .models import Company


class SingleComView(DetailView):
    template_name = "Company/SingleCom.html"
    model = Company


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
