from django.shortcuts import render
from django.http import JsonResponse
from students.models import Students

# Create your views here.
def studentViews(request):
    students = Students.objects.all()
    #serializing the data
    students_list = list(students.values())
    return JsonResponse(students_list,safe=False)