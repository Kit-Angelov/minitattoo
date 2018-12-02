from django.shortcuts import render
from .models import *


def index(request):
    pics = Pic.objects.all()
    context = {
        "pics": pics,
    }
    return render(request, 'app/index.html', context=context)
