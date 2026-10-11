
from django.shortcuts import render



def home(request):
    goals = [
        {"name": "Start my personal website", "completed": True},
        {"name": "Complete employee monthly assessments", "completed": False},
        {"name": "Complete a new hiking trail", "completed": True},
        {"name": "Read 2 more books", "completed": False},
        {"name": "Attend 1 painting class", "completed": False},
    ]

    return render(request, "home.html", {"goals": goals})



def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")
