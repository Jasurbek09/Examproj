from django.shortcuts import render
from main.models import *

# Create your views here.


def indexHandler(request):
    team = National_team.objects.all().order_by('name')[:4]

    group = Group.objects.all()
    return render(request, 'index2.html', {'team': team,
                                           'group': group})
