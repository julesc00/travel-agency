from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        "moto": "The framework for perfectionist!"
    }

    return render(request, "app/index.html", context)
