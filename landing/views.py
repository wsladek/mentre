from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse("What the what's up doc?")

    return render(request, 'landing/index.html')