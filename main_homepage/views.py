from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def main_homepage(request):
    return render(request=request, template_name="main_homepage/index.html")