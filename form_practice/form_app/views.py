from django.shortcuts import render
from .forms import contactForm, StudentData


# Create your views here.
def home(request):
    return render(request, "home.html")


def about(request):
    if request.method == "POST":
        name = request.POST.get("username")
        email = request.POST.get("email")
        select = request.POST.get("select")
        return render(
            request, "about.html", {"name": name, "email": email, "select": select}
        )
    else:
        return render(request, "about.html")


def submit_form(request):
    return render(request, "form.html")


def django_form(request):
    if request.method == "POST":
        form = contactForm(request.POST, request.FILES)
        if form.is_valid():
            # file = form.cleaned_data["file"]
            # with open("./form_app/upload/" + file.name, "wb+") as destination:
            #     for chunk in file.chunks():
            #         destination.write(chunk)
            print(form.cleaned_data)
    else:
        form = contactForm()
    return render(request, "django_form.html", {"form": form})


def student_form(request):
    if request.method == "POST":
        form = StudentData(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = StudentData()
    return render(request, "django_form.html", {"form": form})
