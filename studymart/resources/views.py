from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def free_course(request):
    return render(request, 'resources/freecourse.html', {'fcrs':5, 'platform':'StudyMart'} )

def blog(request):
    course1 = 'Machine Learning'
    course2 = 'Deep Learning'
    course3 = 'Data Analysis'
    course4 = 'Python with problem solving'
    freeCourseDetails = {'c1':course1, 'c2':course2, 'c3':course3,'c4':course4}
    return render(request, 'resources/blog.html', freeCourseDetails)

