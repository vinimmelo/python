from django.shortcuts import render
from django.http import HttpResponse

#Follow the convention about insert the html page inside the 'templates' folder!!!
def index(request):
    return render(request, 'index.html')
