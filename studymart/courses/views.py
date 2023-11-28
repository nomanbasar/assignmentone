from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def course(request):
    return HttpResponse('Welcome to Django')

def Data_Science(request):
    available_course = {'fcourse':['ML','DL','DA','DJ','Python']}
    return render(request, 'courses/datascience.html', available_course)

def Big_Data(request):
    return render(request, 'courses/bigdata.html')

def Data_Analysis(request):
    return HttpResponse('Welcome to Data Analysis')

def Deep_Learning(request):
    return HttpResponse('Welcome to Deep Learning')
